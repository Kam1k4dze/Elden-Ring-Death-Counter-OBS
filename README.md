# Automatic Elden Ring death counter OBS script
### Скрипт для OBS, автоматический устанавливающий смерти в Elden Ring
![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg) ![GitHub Repo stars](https://img.shields.io/github/stars/vadimkacool/Elden-Ring-Death-Counter-OBS?color=gree)
## Преимущества

- Нет необходимости импользовать скрипт с самого начала игры, он автоматически загрузит предыдущие смерти, которые были до его установки
- Нет необходимости каждый раз нажимать на кнопку после смерти, скрипт обновляет данные автоматически
## Установка
#### 0.Скачайте [скрипт](https://github.com/Sphynx-HenryAY/elden-ring-death-counter/archive/refs/heads/main.zip)

#### 1.Python
 - Скачайте [Python](https://www.python.org/downloads/release/python-3109/)
 - Установите (*Поставьте галочку добавить в PATH во время установки*)

#### 2.Установите зависимости
- Откройте командную строку(`Win+R`)
   1. Нажмите Win+R
   2. Введите `cmd`
- Выполните в Командной строке
```sh
pip install pymem
```

#### 3. Установка в OBS
1. Зайдите в OBS
2. Выберите на панели сверху `Сервис`->`Скрипты`
3. Выберите сверху `Настройки Python`
4. Выберите папку, где установлен Python
    - Для того, чтобы узнать путь установки Python введите это в командную строку
      ```sh
      python -c "import os, sys; print(os.path.dirname(sys.executable))"
      ```
- Вернитесь на вкладку скрипты и нажмите на `+`
- Выберите, ранее скачанный, файл `DeathCounter.py`

## Использование
1. Создайте Текст(GDI+) в вашей сцене
2. Введите его название в `Source` в меню скрипта
3. Запустите Elden Ring без антчита
    - Поместите файл `offline_launcher.bat` в папку с игрой(`steamapps\common\ELDEN RING\Game`)
    - Запускайте игру с помощью этого файла.
4. После загрузки и входа в игру, нажмите на кнопку `Attach` в меню скрипта. Скрипт должен обновить созданный вами ранее текст. Далее скрипт будет обновлять смерти автоматически

## Если данный скрипт вам помог, поставьте ему ⭐
