# -*- coding: utf-8 -*-

from flask import jsonify
from fuploader.fuploader_blueprint import fuploader

@fuploader.route('/upload')
def upload():
    return jsonify(err=200)