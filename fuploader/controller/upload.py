# -*- coding: utf-8 -*-

import os
from flask import jsonify, request, current_app, render_template
from werkzeug.utils import secure_filename
from fuploader.fuploader_blueprint import fuploader

@fuploader.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'GET':
        return render_template('upload.html')
    elif request.method == 'POST':
        save_filename = ''
        try:
            upload_file = request.files['file']
            upload_dir = current_app.config['UPLOAD_DIR']

            if not os.path.exists(upload_dir):
                os.makedirs(upload_dir)

            save_filename = os.path.join(upload_dir, secure_filename(upload_file.filename))
            upload_file.save(save_filename)
        except:
            return render_template('upload_result.html', result="FAIL", filename=save_filename)

    return render_template('upload_result.html', result="SUCCESS", filename=save_filename)