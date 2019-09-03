from . import *
import cv2 as cv
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser("magic wand selector")
    parser.add_argument("image", help="path to image")
    args = parser.parse_args()

    img = cv.imread(args.image)
    if img is None or img.size == 0:
        raise Exception(f"Unable to read image {args.image}. Please check the path.")

    window = SelectionWindow(img, "Magic Wand Selector")

    print("Click to seed a selection.")
    print("[shift] adds to a selection.")
    print("[alt] subtracts from a selection.")
    print("[shift] + [alt] intersects the selections.")

    window.show()
    cv.destroyAllWindows()
