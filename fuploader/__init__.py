# -*- coding: utf-8 -*-

from flask import Flask, request, url_for
from fuploader.controller import index, upload
from fuploader.module.logger import Log
from fuploader.module.configmanager import ConfigManager

def url_for_other_page(page):
    args = request.view_args.copy()
    args['page'] = page
    return url_for(request.endpoint, **args)

def create_app(argv):
    fupload_app = Flask(__name__)

    configmanager = ConfigManager()
    Log.init(log_path=configmanager.LOG)
    Log.info("-------------------- Starting File Upload Server... --------------------")
    configmanager.print_settings()

    from fuploader.fuploader_blueprint import fuploader
    fupload_app.register_blueprint(fuploader)

    fupload_app.jinja_env.globals['url_for_other_page'] = url_for_other_page

    return fupload_app