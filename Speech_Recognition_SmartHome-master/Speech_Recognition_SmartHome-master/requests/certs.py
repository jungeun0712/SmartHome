#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
requests.certs
~~~~~~~~~~~~~~

This module returns the preferred default CA certificate bundle.

If you are packaging Requests, e.g., for a Linux distribution or a managed
environment, you can change the definition of where() to return a separately
packaged CA bundle.
"""
import os.path

try:
    from certifi import where
except ImportError:
    def where():
        """Return the preferred certificate bundle."""
        # On Debian systems use ca-certificates
        return '/etc/ssl/certs/ca-certificates.crt'

if __name__ == '__main__':
    print(where())
