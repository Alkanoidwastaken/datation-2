import pip

def import_or_install(package):
    try:
        __import__(package)
    except ImportError:
        pip.main(['install', package])

import_or_install('PyInstaller')

import PyInstaller

PyInstaller.__main__.run([
    'main.py',
    '--onefile',
])