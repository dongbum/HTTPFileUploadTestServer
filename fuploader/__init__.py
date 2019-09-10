# -*- coding: utf-8 -*-

from flask import Flask, request, url_for
from fuploader.controller import index, upload
from fuploader.module.logger import Log

def print_settings(config):
    Log.info('===================================================================')
    Log.info('settings for FileUploadTest-Server')
    Log.info('===================================================================')
    for key, value in config:
        Log.info('%s=%s' % (key, value))
    Log.info('===================================================================')

def url_for_other_page(page):
    args = request.view_args.copy()
    args['page'] = page
    return url_for(request.endpoint, **args)

def create_app(argv):
    fupload_app = Flask(__name__, instance_relative_config=True)

    fupload_app.config.from_pyfile(str(argv[1]), silent=True)

    Log.init(log_path=str(fupload_app.config['LOG']))
    Log.info("-------------------- Starting File Upload Server... --------------------")
    Log.info('InstancePath:[%s]' % fupload_app.instance_path)
    print_settings(fupload_app.config.items())

    from fuploader.fuploader_blueprint import fuploader
    fupload_app.register_blueprint(fuploader)

    fupload_app.jinja_env.globals['url_for_other_page'] = url_for_other_page

    return fupload_app