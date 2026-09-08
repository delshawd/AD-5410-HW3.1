from PixelFunctions import storePixels, grayscale, pixels_to_points, pixels_to_image
from SortFunctions import mergeSort
from SearchFunctions import binary_search_sub
from PIL import Image

import colorsys
def main():
    IMG_NAME = 'FCB_small'

    with Image.open(IMG_NAME + '.jpg') as im:
        pixels, yiq_pixels = storePixels(im)
        print("stored")
        mergeSort(yiq_pixels)
        sorted_im = pixels_to_image(im, yiq_pixels)
        sorted_im.save('sorted_' + IMG_NAME + '.jpg', 'JPEG')
        print("sorted")

        target = (183 / 255, 198 / 255, 144 / 255)
        yiq_target = colorsys.rgb_to_yiq(target[0], target[1], target[2])

        subi = binary_search_sub([r[0][0] for r in yiq_pixels],
                                 0, len(yiq_pixels) - 1, yiq_target[0])

        print("target found at: ", subi)

        reverse = False
        choice = ''
        tolerance = int(len(yiq_pixels) / 4)

        while choice.upper() != 'Q':

            grayscale(im, pixels)

            if reverse:
                pixels_to_points(im, yiq_pixels[subi:])
            else:
                pixels_to_points(im, yiq_pixels[:subi])

            choice = input("Q = save and quit, R = reverse, T = tolerance, C = color: ")

            if choice.upper() == 'R':
                reverse = not reverse

            elif choice.upper() == 'T':
                if reverse:
                    subi = subi - tolerance
                else:
                    subi = subi + tolerance

            elif choice.upper() == 'C':
                r = int(input("Enter R: "))
                g = int(input("Enter G: "))
                b = int(input("Enter B: "))

                target = (r / 255, g / 255, b / 255)
                yiq_target = colorsys.rgb_to_yiq(target[0], target[1], target[2])

                subi = binary_search_sub([r[0][0] for r in yiq_pixels],
                                         0, len(yiq_pixels) - 1, yiq_target[0])

            elif choice.upper() == 'Q':
                im.save('highlighted_' + IMG_NAME + '.jpg', 'JPEG')


if __name__ == "__main__":
    main()