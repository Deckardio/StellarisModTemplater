from PIL import Image
from os import listdir, mkdir, path
import argparse
from rich.progress import track
from rich import print


def main(mod_name, folder):
    create_folder(mod_name)
    iter = 0
    for entry in track(listdir(f'{folder}/'),description=f'[green]Processing ...', total=len(listdir(f'{folder}/'))):
            if entry.endswith('.dds'):
                try:
                    image = remove_transparency(Image.open(f'{folder}/{entry}'))
                    new_img = scale_img(image, 380)
                    new_img.save(f'{mod_name}/gfx/models/portraits/{mod_name}{iter}.dds')
                    iter += 1
                except:
                    print(f'[red]{entry} is not a valid image')
    folder = f'{mod_name}/gfx/models/portraits/'
    create_species(mod_name, read_folder(folder, mod_name))
    config_class(mod_name)
    print(f'[green]Mod [blue]{mod_name} [green]created')


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
    cli = argparse.ArgumentParser()
    cli.add_argument('-m', '--mod_name', help='Name of the mod', required=True)
    cli.add_argument('-f', '--folder', help='Folder containing the portraits', required=True)
    args = cli.parse_args()
    mod_name = args.mod_name
    folder = args.folder
    if path.isdir(folder) == False:
        print(f'[red]{folder} is not a valid folder')
        exit()
    elif listdir(folder) == []:
        print(f'[red]{folder} is empty')
        exit()
    elif mod_name == '':
        print(f'[red]{mod_name} is empty')
        exit()
    elif path.isfile('./race_name') == False:
        print(f'[red]race_name is not exist')
        exit()
    else:
        try:
            main(mod_name, folder)
        except:
            print('[red]Something went wrong or ')
