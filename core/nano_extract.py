from PIL import Image
import base64,json
from cryptography.fernet import Fernet

def extract(nano_image):
    img = Image.open(nano_image)

    encrypted = img.text["nano"]
    key = img.text["key"]

    f = Fernet(key.encode())
    data = json.loads(f.decrypt(encrypted.encode()))

    for name,content in data.items():
        with open("data/out_"+name,"wb") as w:
            w.write(base64.b64decode(content))
