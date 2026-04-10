import sys
import os
import logging
from pygame import mixer


logger = logging.getLogger(name=__name__)
logger.setLevel(level=logging.INFO)

console_handler = logging.StreamHandler()
file_handler = logging.FileHandler(filename='logs.log', mode='a')
console_handler.setLevel(logging.INFO)
file_handler.setLevel(logging.INFO)
# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)
logger.addHandler(console_handler)
logger.addHandler(file_handler)

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS  # PyInstaller temp folder
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def space_audio():
    """Background music"""
    bg_audio = resource_path(r'assets\audio\freesound_community-space-adventure-29296.mp3')
    mixer.init()
    mixer.music.load(bg_audio)
    mixer.music.play(loops=-1)  # Play the music (-1 means loop forever)
    logger.info(f"Background music playing {bg_audio}")

