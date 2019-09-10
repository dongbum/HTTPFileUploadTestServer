# -*- coding: utf-8 -*-

import sys
from fuploader import create_app

application = create_app(sys.argv)

if __name__ == '__main__':
    print("starting file upload server...")

    application.run(host='0.0.0.0', port=application.config['PORT'], debug=True)