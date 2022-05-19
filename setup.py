from setuptools import setup
from setuptools.command.develop import develop
from setuptools.command.install import install
from subprocess import check_call
class InstallGit(install):
    def run(self):
        check_call("apk add git".split())
        install.run(self)
class InstallAlpineFfmpeg(install):
    def run(self):
        check_call("pip install git+https://git@github.com:nitrogate/alpine-ffmpeg@master".split())
        install.run(self)   
class InstallFfmpeg(install):
    def run(self):
        check_call("apk add ffmpeg".split())
        install.run(self)     

setup(name='alpine-ffmpeg',
      version='0.1',
      description='Install ffmpeg inside openruntimes Docker container',
      url='https://github.com/nitrogate/alpine-ffmpeg.git',
      author='Nitrogate',
      author_email='nitrogate@gazeta.pl',
      license='GNU GPL 3.0',
      packages=['alpine-ffmpeg'],
      zip_safe=False,
      cmdclass={ "install": [InstallGit, InstallAlpineFfmpeg, InstallFfmpeg] })
