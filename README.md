# Modelo 🧠 "Red Neuronal Convolucional"🧠

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Conda](https://img.shields.io/badge/Conda-env-green)
![Torch](https://img.shields.io/badge/PyTorch-CUDA-orange)
![Ultralytics](https://img.shields.io/badge/Ultralytics-YOLOv8-yellow)
![Docker](https://img.shields.io/badge/Docker-LabelStudio-lightblue)

# ⚠️ Importante
Este proyecto **debe ejecutarse en un entorno de desarrollo Linux** o, en su defecto, utilizando **WSL (Windows Subsystem for Linux)**.



## Instalar Anaconda
~~~~
sudo apt-get update && sudo apt-get upgrade
sudo apt install wget -y
~~~~

## Instalacion de dependencias necesarias
~~~~
sudo apt-get install libgl1 libglx-mesa0 libxrandr2 libxrandr2 libxss1 libxcursor1 libxcomposite1 libxi6 libxtst6
sudo apt-get install libasound2t64
sudo apt install zip unzip -y
~~~~

## Instalar anaconda
~~~~
wget https://repo.anaconda.com/archive/Anaconda3-2025.06-1-Linux-x86_64.sh
bash Anaconda3-2025.06-1-Linux-x86_64.sh
~~~~

## Comprobar instalacion
- para este paso es necesario agregar al PATH la configuración de Anaconda 
~~~~
conda --version
conda update conda
~~~~

## Crear enviroment para el modelo
~~~~
conda create --name fede-model-env1 python=3.13
~~~~

## Activar el enviroment
~~~~
conda activate fede-model-env1
~~~~

## Desactivar el enviroment
~~~~
conda deactivate
~~~~

esta seccion hace referencia al 
## Pullear label studio (para etiquetado)
~~~~
docker pull heartexlabs/label-studio:latest
~~~~

## Activar label studio (para etiquetado)
~~~~
sudo docker start label-studio

sudo docker run -d -p 8080:8080 --user 1000:1000 -v $(pwd)/mydata:/label-studio/data -e LABEL_STUDIO_LOCAL_FILES_SERVING_ENABLED=true -e LABEL_STUDIO_LOCAL_FILES_DOCUMENT_ROOT=/label-studio/data heartexlabs/label-studio:latest

O este:
sudo docker run -d --name label-studio \
  -p 8080:8080 \
  --user 1000:1000 \
  -v "$PWD/mydata:/label-studio/data" \
  -e LABEL_STUDIO_LOCAL_FILES_SERVING_ENABLED=true \
  -e LABEL_STUDIO_LOCAL_FILES_DOCUMENT_ROOT=/label-studio/data \
  heartexlabs/label-studio:latest

~~~~

sudo docker start label-studio

## Instalar dependencias dentro del enviroment
~~~~
conda activate fede-model-env1
pip install ipykernel
pip install ultralytics
~~~~

## Version general
~~~~
pip3 install torch torchvision --index-url https://download.pytorch.org/whl/cu130
~~~~

### Para 1050TI
~~~~
pip install torch==2.7.1+cu118 torchvision==0.22.1+cu118 torchaudio==2.7.1+cu118 --index-url https://download.pytorch.org/whl/cu118
~~~~

# Utilizar modelo 

- Para Windows PowerShell o Anaconda Prompt
~~~~
(Abrir terminal de Conda (Windows))
conda init powershell
conda activate fede-model-env1
python utils/yolo_detect.py --model my_model/my_model.pt --source usb0 --resolution 1280x720
~~~~

- En WSL/Linux 
~~~~
conda activate fede-model-env1
cd  ruta del modelo : pmai-model-vision
python utils/yolo_detect.py --model my_model/my_model.pt --source 0 --resolution 1280x720
~~~~

