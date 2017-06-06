# -*- coding: utf-8 -*-

from glob import glob

DISTUTILS_DEBUG = "True"


try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

config = {}

config['classifiers'] = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: GNU General Public License (GPL)',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: C',
    'Programming Language :: Python',
    'Programming Language :: JavaScript',
    'Topic :: Scientific/Engineering',
    'Topic :: Software Development :: Code Generators',
]

setup(name='harpia',
      install_requires=['mosaicomponents', 'beautifulsoup4',
                'pip', 'Python>=2.7'],
      tests_require=['pytest'],
      test_suite='test',
      version='1.0a7',
      packages=[
          'app_data',
          'harpia',
          'harpia.utils',
          'harpia.persistence',
          'harpia.GUI',
          'harpia.extensions',
          'harpia.extensions.c',
          'harpia.extensions.c.opencv',
          'harpia.extensions.c.ports',
          'harpia.extensions.javascript',
          'harpia.extensions.javascript.webaudio',
          'harpia.extensions.javascript.ports',
          'harpia.control',
          'harpia.model'],
      scripts=['launcher/harpia', 'scripts/harpia.sh','scripts/harpia.1'],
      description='Image Processing and Computer Vision \
      Automatic Programming Tool',
      author='Ouroboros',
      author_email='cmagnobarbosa+harpia@gmail.com',
      maintainer="Ouroboros",
      maintainer_email="cmagnobarbosa+harpia@gmail.com",
      license="GNU GPL3",
      url='http://ges.dcomp.ufsj.edu.br/index.php/ouroboros/',

      # this is fucked up! must put it in package_data!!
      data_files=[
            ('/usr/share/harpia/images', glob("app_data/images/*")),
            ('/usr/share/harpia/po/pt/LC_MESSAGES/',
                   glob("app_data/po/pt/LC_MESSAGES/*")),
            ('/usr/share/harpia/examples', glob("app_data/examples/*.hrp")),
            ('/usr/share/applications/', ["app_data/harpia.desktop"]),
            ('/usr/share/icons/hicolor/scalable/apps',
                   ['app_data/images/harpia.svg']),
            ('/usr/share/pixmaps', ['app_data/images/harpia.svg']),
            ('/usr/share/icons/hicolor/24x24/apps',
                   ['app_data/images/harpia.png']), ],
      **config
      )
