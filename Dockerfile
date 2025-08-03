FROM nvidia/cuda:11.8.0-cudnn8-runtime-ubuntu22.04

# Sistem ve Python bağımlılıkları
RUN apt update && apt install -y git wget curl python3 python3-pip

# Python pip bağlantısı
RUN ln -s /usr/bin/python3 /usr/bin/python

# Python bağımlılıkları
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install --upgrade pip && pip install -r requirements.txt

# TripoSR modelini kopyala
COPY tripo /workspace/tripo

# Model indirici scripti çalıştır
COPY download_model.sh /workspace/download_model.sh
RUN bash /workspace/download_model.sh

# Çalışma klasörünü ayarla
WORKDIR /workspacea

# RunPod handler dosyasını kopyala
COPY handler.py .

# RunPod için başlangıç komutu
CMD ["python", "handler.py"]