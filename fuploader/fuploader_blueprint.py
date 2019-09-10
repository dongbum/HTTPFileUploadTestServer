# -*- coding: utf-8 -*-

from flask import Blueprint

fuploader = Blueprint('lcsrv', __name__, template_folder='../templates', static_folder='../static')