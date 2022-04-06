# setup/install file

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description'       :   'Valid Sentence',
    'author'            :   'Paul Rafferty',
    'url'               :   'https://github.com/paulrafferty/validsentence',
    'download_url'      :   'https://github.com/paulrafferty/validsentence',
    'author_email'      :   'paulrafferty@outlook.com',
    'version'           :   '0.1',
    'install_requires'  :   [],
    'packages'          :   ['validsentence'],
    'scripts'           :   [],
    'name'              :   'validsentence'
}

setup(**config)
