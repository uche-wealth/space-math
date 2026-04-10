import sys
import os
import logging
from pygame import mixer


logging.basicConfig(level=logging.INFO)

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
    logging.info(f"Background music playing {bg_audio}")

