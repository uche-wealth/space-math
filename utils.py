import sys
import os
import logging
from datetime import datetime
from pygame import mixer
from pathlib import Path
from collections import deque

class Logger:
    """Handle logging"""
    def __init__(self, name=__name__):
        self.log_file = Path('__logs.log')
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level=logging.INFO)
        # handlers
        self.console_handler = logging.StreamHandler()
        self.file_handler = logging.FileHandler(filename=self.log_file, mode='a', encoding='utf-8')
        self.console_handler.setLevel(logging.INFO)
        self.file_handler.setLevel(logging.INFO)
        # create formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.console_handler.setFormatter(formatter)
        self.file_handler.setFormatter(formatter)
        self.logger.addHandler(self.console_handler)
        self.logger.addHandler(self.file_handler)


class Helpers:
    """Helper class"""
    def __init__(self, base_path=''):
        self.base_path = base_path

    def _resource_path(self, relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        try:
            base_path = sys._MEIPASS  # PyInstaller temp folder
        except AttributeError:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

    def _space_audio(self):
        """Background music"""
        bg_audio = self._resource_path(r'assets\audio\freesound_community-space-adventure-29296.mp3')
        mixer.init()
        mixer.music.load(bg_audio)
        mixer.music.play(loops=-1)  # Play the music (-1 means loop forever)
        log = Logger().logger
        log.info(f"Background music playing {bg_audio}")

