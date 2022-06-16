# StellarisModTemplater
Image-based template generator for creating Stellaris mods. All you need to do is specify a folder with images in dds format. The images will be adjusted to the game height of 380 with transparency removed from the edges and proportions preserved.
# Installation
Install the module from requirements.txt
```bash
git clone https://github.com/Deckardio/StellarisModTemplater.git
```
```bash
cd StellarisModTemplater
```
```bash
pip3 install -r requirements.txt
```

# Quick start
```bash
usage: StellarisModTemplater.py -m MOD_NAME -f FOLDER

exemple: StellarisModTemplater.py -m "My mod name" -f "Images folder"
```
For work with the module, you need to specify the name of the mod and the folder with .dds format images. Also you need to have the species_classes file (called `race_name`) in the same folder as main script. Thats need for create class file in `ModName`\common\species_classes\00`ModName`classes.txt. Script replace `OUR_SPECIE_NAME` in race_name file to you mod name.