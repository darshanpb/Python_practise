# -*- coding: utf-8 -*-
''' insecure password locker '''
password = {
    "email":"abcd",
    "blog":"a12b"
}

import sys
import pyperclip
if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
sys.exit()
account = sys.argv[1] # first command line arg is the account name
if account in password:
    pyperclip.copy(password[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)