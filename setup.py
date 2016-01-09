try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Python3 wrapper for ffprobe',
    'author': 'Alexander Young',
    'url': 'http://github.com/alexanderpyoung/pyffprobe',
    'download_url':'http://github.com/alexanderpyoung/pyffprobe',
    'author_email': 'alexander@lxndryng.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['pyffprobe'],
    'scripts': [],
    'name': 'pyffprobe'
}

setup(**config)
