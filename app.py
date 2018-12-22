#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from Project import *
from gevent.pywsgi import WSGIServer

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10095))
    app.run('127.0.0.1', port=port, threaded=True, debug=True)
    # app.run(ssl_context='adhoc', port=port) # HTTPS

    # Serve the app with gevent
    # http_server = WSGIServer(('127.0.0.1', port), app)
    # http_server.serve_forever()
