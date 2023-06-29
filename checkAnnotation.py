import os, sys
import cv2
import matplotlib.pyplot as plt

labels_path = './Labels/full_catAndDog/'
image_path = './Images/full_catAndDog/'


def check(label_name):
    #read file
    label_abs_path = labels_path + label_name + '.txt'
    labels_file = open(label_abs_path, 'r')
    line = [l[:-1] for l in labels_file.readlines() if len(l) > 1][0]
    labels_file.close()
    line = [float(l) for l in line.split(' ')]
    print('Params: ', line)
    image_file = image_path + label_name + '.jpg'
    image = cv2.imread(image_file)
    H, W, _ = image.shape
    image = cv2.rectangle(image, (int(W * (line[1] - line[3] / 2)), int(H * (line[2] - line[4] / 2))),
                        (int(W * (line[1] + line[3] / 2)), int(H * (line[2] + line[4] / 2))), (0, 255, 0), 3)
    print('Coordinates: ', int(W * (line[1] - line[3] / 2)), int(H * (line[2] - line[4] / 2)), int(W * (line[1] + line[3] / 2)), int(H * (line[2] + line[4] / 2)))
    plt.imshow(image)
    plt.show()


def main():
    args = sys.argv[1:]
    if len(args) <= 0:
        print('Not the right number of arguments, use -h for usage recommendations')
        return
    elif args[0] == '-h':
        if len(args) > 1:
            print('Not the right number of arguments, for this feature, only -h args is accepted')
        else:
            print('-h: for helper ; -v annotation txt name: name of the arguments txt to verify with the image ')
    elif args[0] == '-v':
        if len(args) > 2:
            print('Not the right number of arguments, use -h for usage recommendations')
        elif len(args) == 2:
            if not os.path.exists(labels_path + args[1] + '.txt'):
                print('Please enter the path to file, use -h for usage recommendations')
            else:
                check(args[1])
        else:
            print('Not the right number of arguments, use -h for usage recommendations')
    else:
        print('Not correct usage, use -h for usage recommendation')


if __name__ == '__main__':
    main()
