#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from Project import *

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8001))
    app.run('192.168.1.232', port=port)
    # app.run(ssl_context='adhoc', port=port) # HTTPS
