#!/usr/bin/env python

from passlib.hash import sha512_crypt
import getpass

# passlib 1.6.1
print sha512_crypt.encrypt(getpass.getpass(), rounds=5000)

