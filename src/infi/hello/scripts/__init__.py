from __future__ import print_function
__import__("pkg_resources").declare_namespace(__name__)

from sys import argv
import os

INSTALLDIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))

def main(argv=argv):
    print('hello world')

def _write_file(name):
    with open(os.path.join(INSTALLDIR, name), 'w') as fd:
        fd.write(' ')

def post_install(argv=argv):
    _write_file('post_install')

def pre_uninstall(argv=argv):
    config = os.path.join(INSTALLDIR, 'config')
    if not os.path.exists(config):
        os.mkdir(config)
    _write_file(os.path.join('config', 'pre_uninstall'))

