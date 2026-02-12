from core.ocr import read_image
from core.translator import translate
from core.nano_embed import embed
from core.nano_extract import extract

print("OCR:", read_image("data/input.png"))
print("Translated:", translate(read_image("data/input.png"),"th"))

embed("data/input.png",["data/payload.pdf"],"nano")

extract("data/nano.png")
