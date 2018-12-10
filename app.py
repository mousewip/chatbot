#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from Project import *

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10095))
    app.run('127.0.0.1', port=port)
    # app.run(ssl_context='adhoc', port=port) # HTTPS
