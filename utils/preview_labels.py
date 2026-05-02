import cv2
import os
from pathlib import Path
import ast


def load_class_names(config_path="data.yaml"):
    config_file = Path(config_path)
    if not config_file.exists():
        return []

    names = []
    in_names_block = False

    with open(config_file, "r", encoding="utf-8") as f:
        for raw_line in f:
            line = raw_line.strip()

            if line == "names:":
                in_names_block = True
                continue

            if in_names_block:
                if line.startswith("- "):
                    value = line[2:].strip()
                    if value.startswith(("'", '"')) and value.endswith(("'", '"')):
                        try:
                            value = ast.literal_eval(value)
                        except (ValueError, SyntaxError):
                            value = value.strip("'\"")
                    names.append(value)
                    continue

                if line:
                    break

    return names


def get_class_label(cls_id, class_names):
    if cls_id.is_integer():
        cls_index = int(cls_id)
        if 0 <= cls_index < len(class_names):
            return class_names[cls_index]
        return str(cls_index)
    return f"{cls_id:.2f}"


def draw_bboxes(images_path, labels_path, output_path, class_names=None, max_images=200):
    output_path = Path(output_path)
    output_path.mkdir(parents=True, exist_ok=True)
    class_names = class_names or []

    extensions = ["*.jpg", "*.jpeg", "*.png"]
    images = []
    for ext in extensions:
        images.extend(list[Path](Path(images_path).glob(ext)))

    images = images[:max_images]

    for img_path in images:
        label_path = Path(labels_path) / (img_path.stem + ".txt")
        if not label_path.exists():
            print(f"Sin label => {img_path.name}")
            continue
        
        img = cv2.imread(str(img_path))
        if img is None:
            print(f"ERROR leyendo imagen => {img_path}")
            continue

        h, w = img.shape[:2]

        with open(label_path, "r") as f:
            lines = f.readlines()

        for line in lines:
            parts = line.strip().split()
            if len(parts) != 5:
                print(f"Label inválido => {label_path}")
                continue

            cls, x, y, bw, bh = map(float, parts)

            x1 = int((x - bw/2) * w)
            y1 = int((y - bh/2) * h)
            x2 = int((x + bw/2) * w)
            y2 = int((y + bh/2) * h)

            class_label = get_class_label(cls, class_names)
            cv2.rectangle(img, (x1, y1), (x2, y2), (0,255,0), 2)
            cv2.putText(img, class_label, (x1, y1 - 5),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)

        out_file = output_path / f"{img_path.stem}_preview.jpg"
        cv2.imwrite(str(out_file), img)

    print(f"✔ Previews generados en: {output_path}")

def preview_labels(data_path):
    train_images_path = os.path.join(data_path, "train", "images")
    train_labels_path = os.path.join(data_path, "train", "labels")
    validation_images_path = os.path.join(data_path, "validation", "images")
    validation_labels_path = os.path.join(data_path, "validation", "labels")

    class_names = load_class_names("data.yaml")

    draw_bboxes(train_images_path, train_labels_path, "previews/preview_train", class_names=class_names)

    draw_bboxes(validation_images_path, validation_labels_path, "previews/preview_val", class_names=class_names)

