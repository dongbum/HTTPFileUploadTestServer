# -*- coding: utf-8 -*-

import sys
from fuploader import create_app
from fuploader.module.configmanager import ConfigManager

application = create_app(sys.argv)

if __name__ == '__main__':
    print("starting file upload server...")
    configmanager = ConfigManager()
    application.run(host='0.0.0.0', port=configmanager.PORT, debug=True)