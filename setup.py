import subprocess
from setuptools import setup

from setuptools import setup
from setuptools.command.develop import develop
from setuptools.command.install import install

def install_ffmpeg():
    try:
        subprocess.run(["apk", "add", "ffmpeg"], check=True)
    except subprocess.CalledProcessError:
        pass

class PostInstallCommand(install):
    def run(self):
        install.run(self)
        install_ffmpeg()

setup(name='alpine-ffmpeg',
      version='0.1',
      description='Install ffmpeg inside openruntimes Docker container',
      url='https://github.com/nitrogate/alpine-ffmpeg.git',
      author='Nitrogate',
      author_email='nitrogate@gazeta.pl',
      license='GNU GPL 3.0',
      packages=['alpine-ffmpeg'],
      zip_safe=False,
      cmdclass={ "install": PostInstallCommand })