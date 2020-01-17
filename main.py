from PIL import Image

# Enter PNG/JPG File Name Here in same directory as file
image = Image.open("Here").convert('RGB')
px = image.load()
width, height = image.size


def catchType(message, err_msg, t):
    while True:
        try:
            return t(t(input(message)))
        except ValueError:
            print(err_msg)
            pass


def pixelAscii(lightlevel, brightness_ascii):
    temp = float('inf')
    for key in brightness_ascii:
        if lightlevel < key < temp:
            temp = key
    return brightness_ascii.get(temp, ' ')


def shadeGeneration(shadeLevel):
    shader = ['$', '@', 'B', '%', '8', '&', 'W', 'M', '#', '*', 'o', 'a', 'h', 'k', 'b', 'd', 'p', 'q', 'w', 'm', 'Z',
              'O', '0', 'Q', 'L', 'C', 'J', 'U', 'Y', 'X', 'z', 'c', 'v', 'u', 'n', 'x', 'r', 'j', 'f', 't', '/', '\\',
              '|', '(', ')', '1', '{', '}', '[', ']', '?', '-', '_', '+', '~', '<', '>', 'i', '!', 'l', 'I', ';', ':',
              ',', '^', '`', "'", '.', ' ']
    brightness_ascii = {}
    value = 255 / shadeLevel
    for shade in range(shadeLevel):
        brightness_ascii[(shade + 1) * value] = shader[shade]
    return brightness_ascii


def startGeneration():
    print(
        '''
        ====
        INFO
        ====        
        '''
    )
    size = catchType('Enter the size of image (1 is largest) ', 'Not a number', int)
    shade = catchType('Enter the shade intensity (max is 69) ', 'not a number', int)
    print('Starting Generation')
    string = ''

    for y in range(0, height, size):
        for x in range(0, width, size):
            string += str(pixelAscii(sum(px[x, y]) / 3, shadeGeneration(shade)))
            string += ' '
        string += '\n'
    string += f'\n Width: {width} Pixels | Height: {height} Pixels | Shade Level: {shade} | Size: {size}'
    return string


def main():
    print(
        '''
        ===============
        ASCII GENERATOR
        ===============

        1: Start Generation
        2: End Generation
        '''
    )
    s = catchType('Enter a Menu: ', 'Not a number', int)
    if s == 1:
        print(startGeneration())
        main()
    else:
        exit()


main()
