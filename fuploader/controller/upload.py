# -*- coding: utf-8 -*-

import os
from flask import request, render_template
from werkzeug.utils import secure_filename
from fuploader.fuploader_blueprint import fuploader
from fuploader.module.configmanager import ConfigManager

@fuploader.route('/upload', methods=['GET', 'POST'])
def upload():
    configmanager = ConfigManager()
    if request.method == 'GET':
        return render_template('upload.html')
    elif request.method == 'POST':
        save_filename = ''
        try:
            upload_file = request.files['file']
            upload_dir = configmanager.UPLOAD_DIR

            if not os.path.exists(upload_dir):
                os.makedirs(upload_dir)

            save_filename = os.path.join(upload_dir, secure_filename(upload_file.filename))
            upload_file.save(save_filename)
        except Exception as ex:
            return render_template('upload_result.html', result="FAIL", filename=save_filename)
        except BaseException:
            return render_template('upload_result.html', result="FAIL", filename=save_filename)
        except SystemExit:
            pass

    return render_template('upload_result.html', result="SUCCESS", filename=save_filename)