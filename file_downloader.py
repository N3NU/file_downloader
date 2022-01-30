#! /usr/bin/env python3

import requests
import sys
import re

url = sys.argv[1]
r = requests.get(url, allow_redirects=True)
file_name = re.findall(r'/([a-zA-Z0-9_\-?.,<>*!@#$%^&()=+;:\'"~`}{]*$)', sys.argv[1])
print(file_name[0])
open(f'{file_name[0]}','wb').write(r.content)
