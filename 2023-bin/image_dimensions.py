from PIL import Image
import sys

def get_image_dimensions(filename):
    with Image.open(filename) as img:
        return img.width, img.height

def main():
    if len(sys.argv) != 2:
        print("Usage: python image_dimensions.py <image_file.png>")
        sys.exit(1)

    image_file = sys.argv[1]
    width, height = get_image_dimensions(image_file)

    print(f"{image_file} {width}x{height}")

if __name__ == "__main__":
    main()
