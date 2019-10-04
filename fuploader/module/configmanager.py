# -*- coding: utf-8 -*-

import os, configparser
from flask import current_app
from fuploader.module.logger import Log

class ConfigManager:
    def __init__(self):
        try:
            if os.path.exists('config.ini'):
                self.config = configparser.ConfigParser()
                self.config.read('config.ini')
                self.PORT = self.config['DEFAULT']['PORT']
                self.LOG = self.config['DEFAULT']['LOG']
                self.UPLOAD_DIR = self.config['DEFAULT']['UPLOAD_DIR']
            else:
                self.PORT = os.environ['PORT']
                self.LOG = os.environ['LOG']
                self.UPLOAD_DIR = os.environ['UPLOAD_DIR']
        except Exception as ex:
            print(ex)
            exit(-1)

    def print_settings(self):
        Log.info('===================================================================')
        Log.info('settings for FileUploadTest-Server')
        Log.info('===================================================================')
        Log.info('PORT=%s' % self.PORT)
        Log.info('LOG=%s' % self.LOG)
        Log.info('UPLOAD_DIR=%s' % self.UPLOAD_DIR)
        Log.info('===================================================================')
