from PIL import Image
from os import listdir, mkdir, path
import re

def scale_img(img, newheight):
    width, height = img.size
    scale = newheight / height
    new_width = int(width * scale)
    img = img.resize((new_width, newheight), Image.ANTIALIAS)
    return img

def remove_transparency(im):
    im.getbbox()
    im2 = im.crop(im.getbbox())
    return im2


def create_folder(mod_name):
    if mod_name not in listdir('.'):
        mkdir(mod_name)
        mkdir(f'{mod_name}/gfx')
        mkdir(f'{mod_name}/common')
        mkdir(f'{mod_name}/common/species_classes')
        mkdir(f'{mod_name}/gfx/models')
        mkdir(f'{mod_name}/gfx/portraits')
        mkdir(f'{mod_name}/gfx/models/portraits')
        mkdir(f'{mod_name}/gfx/portraits/portraits')


def create_species(mod_name, files):
    with open(f'{mod_name}/gfx/portraits/portraits/{mod_name}_species_{mod_name}.txt', 'w') as f:
        f.write('portraits = {\n')
        for line in files:
            f.write('\t%s = { texturefile = "gfx/models/portraits/%s.dds"   }\n' % (line, line))
        f.write('}\n')
        f.write('portrait_groups = {\n\t%s = {\n\t\tdefault = %s\n\t\tgame_setup = { add = { portraits  = { ' % (mod_name, files[0]))
        for line in files:
            f.write(f'{line} ')
        f.write('} } }\n')
        f.write('\t\tpop = { add = { portraits = { ')
        for line in files:
            f.write(f'{line} ')
        f.write('} } }\n')
        f.write('\t\tleader = { add = { portraits = { ')
        for line in files:
            f.write(f'{line} ')
        f.write('} } }\n')
        f.write('\t\truler = { add = { portraits = { ')
        for line in files:
            f.write(f'{line} ')
        f.write('} } } \n')
        f.write('\t}\n}')



def config_class(mod_name):
    with open('race_name', 'r', encoding='utf-8') as f:
        file =  f.read()
    race_name = file.replace('OUR_SPECIE_NAME',mod_name)
    with open(f'{mod_name}/common/species_classes/00{mod_name}classes.txt', 'w') as f:
        f.write(race_name)




def read_folder(folder, mod_name):
    files = []   
    for entry in listdir(folder):
            files.append(entry.split('.')[0])
    files.sort(key=lambda x: int(x.split(f'{mod_name}')[1]))
    return files

if __name__ == '__main__':
    mod_name = 'xyz'
    create_folder(mod_name)
    iter = 0
    for entry in listdir('.'):
            if entry.endswith('.dds'):
                try:
                    image = remove_transparency(Image.open(entry))
                    new_img = scale_img(image, 380)
                    new_img.save(f'{mod_name}/gfx/models/portraits/{mod_name}{iter}.dds')
                    iter += 1
                except:
                    print(f'{entry} is not a valid image')
    folder = f'{mod_name}/gfx/models/portraits/'
    create_species(mod_name, read_folder(folder, mod_name))
    config_class(mod_name)
