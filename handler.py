import runpod
import os
import subprocess
import uuid
import base64

def generate_3d_model(image_bytes):
    # Benzersiz ID
    input_id = str(uuid.uuid4())
    input_path = f"input_{input_id}.png"
    
    # Görseli dosyaya kaydet
    with open(input_path, "wb") as f:
        f.write(image_bytes)

    # Çıktı klasörü
    output_dir = f"output_{input_id}"
    os.makedirs(output_dir, exist_ok=True)

    # TripoSR komutu
    cmd = [
        "python", "tripo/TripoSR/demo.py",
        "--cfg-path", "tripo/TripoSR/configs/demo.yaml",
        "--input-path", input_path,
        "--output-path", output_dir
    ]
    subprocess.run(cmd, check=True)

    # Model dosyasını oku ve base64 encode et
    model_path = os.path.join(output_dir, "output.ply")
    with open(model_path, "rb") as f:
        model_data = f.read()

    return base64.b64encode(model_data).decode("utf-8")

def handler(event):
    image_b64 = event['input'].get('image_base64')
    if not image_b64:
        return {"error": "No image provided."}
    
    image_bytes = base64.b64decode(image_b64)
    model_b64 = generate_3d_model(image_bytes)

    return {"model_base64": model_b64}

runpod.serverless.start({"handler": handler})
