import pip
import os

def import_or_install(package):
    try:
        __import__(package)
    except ImportError:
        pip.main(['install', package])

import_or_install('cpython')

os.system('cython main.py --embed')
os.system("""PYTHONLIBVER=python$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')$(python3-config --abiflags)""")
os.system("""gcc -Os $(python3-config --includes) main.c -o output_bin_file $(python3-config --ldflags) -l$PYTHONLIBVER""")