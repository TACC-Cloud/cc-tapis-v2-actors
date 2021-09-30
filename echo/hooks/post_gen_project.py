#!/usr/bin/env python

"""
Equivalent to 
echo '{}' > secrets.json
"""

with open('secrets.json', 'w') as f:
	f.write('{}')