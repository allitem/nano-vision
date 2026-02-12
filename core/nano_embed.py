from PIL import Image, PngImagePlugin
import base64, json
from cryptography.fernet import Fernet

def embed(image, files:list, password):
    key = Fernet.generate_key()
    fernet = Fernet(key)

    payload = {}
    for f in files:
        payload[f] = base64.b64encode(open(f,'rb').read()).decode()

    encrypted = fernet.encrypt(json.dumps(payload).encode()).decode()

    img = Image.open(image)
    meta = PngImagePlugin.PngInfo()
    meta.add_text("nano", encrypted)
    meta.add_text("key", key.decode())

    img.save("data/nano.png", pnginfo=meta)
