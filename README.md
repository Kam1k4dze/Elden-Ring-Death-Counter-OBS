## [Версия на Русском](README_RU.md)
# Automatic Elden Ring death counter OBS script
### OBS script, automatic Elden Ring death counter
![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg) ![GitHub Repo stars](https://img.shields.io/github/stars/vadimkacool/Elden-Ring-Death-Counter-OBS?color=gree)
## Advantages

- No need to use the script from the beginning of the game, it will automatically load the deaths that were there before it was installed
- No need to press the button every time you die, the script updates the data automatically
## Installation
#### 0.Download [script]https://github.com/vadimkacool/Elden-Ring-Death-Counter-OBS/archive/refs/heads/main.zip)

#### 1.Python
 - Download [Python](https://www.python.org/downloads/release/python-3109/)
 - Install (*Check add to PATH during installation*)

#### 2.Install dependencies.
- Open a command line(`Win+R`)
   - Press Win+R
   - Type `cmd`.
- Execute at the command line
```sh
pip install pymem
```

#### 3. Installing in OBS
1. Go into OBS
2. Select Tools->Scripts in the upper panel.
3. Select from the top "Python Settings".
4. Select the folder where Python is installed
    - To find out the Python installation path, type this into the command line
       ```sh
      python -c "import os, sys; print(os.path.dirname(sys.executable))"
      ```
- Go back to the `Scripts` tab and click on `+`.
- Select, previously downloaded, the ``DeathCounter.py'' file.

## Usage
1. Create Text(GDI+) in your scene
2. Enter it's name in `Source` in the script menu
3. Run Elden Ring without anticheat
    - Put the file `offline_launcher.bat` in the game folder(`steamapps\common\ELDEN RING\Game`)
    - Run the game with this file.
4. After loading and entering the game, click on the `Attach` button in the script menu. The script should update the text you created earlier. The script will then update the deaths automatically

## If this script helped you, give it a ⭐


Translated with www.DeepL.com/Translator (free version)
