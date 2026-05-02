import os
from pathlib import Path
import statistics
import math
from collections import Counter
from PIL import Image

from utils.preview_labels import load_class_names


def gather_bbox_stats(images_dir, labels_dir, sample_limit=None):
    heights = []
    widths = []
    areas = []
    counts = 0

    exts = ['*.jpg', '*.jpeg', '*.png']
    img_paths = []
    for e in exts:
        img_paths.extend(list[Path](Path(images_dir).glob(e)))
    if sample_limit:
        img_paths = img_paths[:sample_limit]

    for img_path in img_paths:
        try:
            with Image.open(img_path) as im:
                W, H = im.size
        except Exception as e:
            continue

        lbl = Path(labels_dir) / (img_path.stem + ".txt")
        if not lbl.exists():
            continue

        with open(lbl, 'r') as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) < 5:
                    continue
                try:
                    _, x, y, w, h = map(float, parts[:5])
                except ValueError:
                    continue
                bw = w * W
                bh = h * H
                ba = bw * bh
                widths.append(bw)
                heights.append(bh)
                areas.append(ba)
                counts += 1

    return {
        'count': counts,
        'widths': widths,
        'heights': heights,
        'areas': areas
    }

def summarize_stats(s):
    if s['count'] == 0:
        return None
    h = s['heights']
    w = s['widths']
    a = s['areas']
    stats = {
        'count': s['count'],
        'height_median': statistics.median(h),
        'height_mean': statistics.mean(h),
        'height_p25': percentile(h,25),
        'height_p75': percentile(h,75),
        'width_median': statistics.median(w),
        'area_median': statistics.median(a)
    }
    return stats

def percentile(data, p):
    if not data:
        return 0
    
    data_sorted = sorted(data)
    k = (len(data_sorted)-1) * (p/100)
    
    f = math.floor(k)
    c = math.ceil(k)
    if f == c:
        return data_sorted[int(k)]
    d0 = data_sorted[int(f)] * (c-k)
    d1 = data_sorted[int(c)] * (k-f)
    return d0 + d1

def recommend_imgsz(height_median):
    if height_median < 16:
        return ">=1024 (recomendado 1280)"
    if height_median < 32:
        return "640 - 1024 (recomendado 1024)"
    if height_median < 64:
        return "512 - 640 (recomendado 640)"
    return "416 - 640 (recomendado 512 o 416 si GPU limitada)"


def count_labels_per_class(labels_dir):
    """Cuenta líneas YOLO válidas (5 valores) por id de clase en todos los .txt."""
    counter = Counter()
    labels_path = Path(labels_dir)
    if not labels_path.is_dir():
        return counter

    for lbl_file in labels_path.glob("*.txt"):
        with open(lbl_file, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) < 5:
                    continue
                try:
                    cls_id = int(float(parts[0]))
                except ValueError:
                    continue
                counter[cls_id] += 1
    return counter


def print_labels_per_class(title, counts, class_names):
    print(f"\n--- Etiquetas por clase ({title}) ---")
    if not counts:
        print("Sin etiquetas.")
        return
    total = sum(counts.values())
    for cls_id in sorted(counts.keys()):
        if 0 <= cls_id < len(class_names):
            name = class_names[cls_id]
        else:
            name = f"clase_{cls_id}"
        print(f"  {name}: {counts[cls_id]}")
    print(f"Total etiquetas: {total}")


def analyze_imgsz():
    train_imgs = os.path.join("data", "train", "images")
    train_lbls = os.path.join("data", "train", "labels")
    val_imgs = os.path.join("data", "validation", "images")
    val_lbls = os.path.join("data", "validation", "labels")

    class_names = load_class_names("data.yaml")

    print("Analizando TRAIN...")
    s_train = gather_bbox_stats(train_imgs, train_lbls)
    train_label_counts = count_labels_per_class(train_lbls)

    print("Analizando VALIDATION...")
    s_val = gather_bbox_stats(val_imgs, val_lbls)
    val_label_counts = count_labels_per_class(val_lbls)

    sum_train = summarize_stats(s_train) if s_train else None
    sum_val = summarize_stats(s_val) if s_val else None

    print("\n--- RESULTADOS TRAIN ---")
    print_labels_per_class("TRAIN", train_label_counts, class_names)
    if sum_train:
        for k,v in sum_train.items():
            print(f"{k}: {v}")
        print("Recomendación imgsz (train):", recommend_imgsz(sum_train['height_median']))
    else:
        print("No se encontraron bboxes en TRAIN.")

    print("\n--- RESULTADOS VALIDATION ---")
    print_labels_per_class("VALIDATION", val_label_counts, class_names)
    if sum_val:
        for k,v in sum_val.items():
            print(f"{k}: {v}")
        print("Recomendación imgsz (val):", recommend_imgsz(sum_val['height_median']))
    else:
        print("No se encontraron bboxes en VALIDATION.")
