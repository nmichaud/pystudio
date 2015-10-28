# -*- coding: utf-8 -*-

# Build standalone executable using cx_Freeze
#
# Run the build process by running the command 'python setup.py build'

###### VERSION ######
version = '0.1.0'
#####################

import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

options = {
    'build_exe': {
        'include_files': ['pystudio'],
        'excludes': ['Tkinter', 'Tk', 'Tcl'],
        'packages': [
            'PyQt4.QtCore',
            'PyQt4.QtGui',
            'hashlib',
            'zmq.backend.cython',
            'zmq.utils.garbage',
            #'enaml',
            'pygments' ,
            'pygments.lexers',
            'pygments.styles',
        ],
    }
}

executables = [
    Executable('__main__.py',
    base=base,
    namespacePackages=['pystudio'],
    icon='pystudio.icns',
    targetName = 'main')
]

setup(
    name          = 'PyStudio',
    version       = version,
    description   = 'PyStudio application',
    author        = 'Naveen Michaud-Agrawal',
    author_email  = 'naveen.michaudagrawal@gmail.com',
    options       = options,
    executables   = executables
)
