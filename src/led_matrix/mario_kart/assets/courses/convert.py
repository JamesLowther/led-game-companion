from PIL import Image
import os

def main():
    files = os.listdir()

    for f in files:
        if os.path.isfile(f) and not f == "convert.py":
            image = Image.open(f)
            image = image.resize((64, 32), Image.Resampling.BOX)
            image = image.convert("RGB")

            d_i = f.find(".")

            image.save(f"{f[:d_i]}.png", format="png")

main()
