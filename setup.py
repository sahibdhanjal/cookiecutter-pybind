import os
import subprocess
import sys
from setuptools import find_packages, setup, Extension
from setuptools.command.build_ext import build_ext
from pathlib import Path

# read the version number for the project
DIR_PATH = os.path.dirname(os.path.realpath(__file__))
VERSION_FILE = os.path.join(DIR_PATH, 'VERSION')

try:
    __version__ = open(VERSION_FILE).read().strip()
except:
    __version__ = '0.0.1'


class CMakeExtension(Extension):
    def __init__(self, name, sourcedir=""):
        Extension.__init__(self, name, sources=[])
        self.sourcedir = os.path.abspath(sourcedir)


class CMakeBuild(build_ext):
    def run(self):
        repo_path = Path(__file__).parent
        subprocess.call(
            ["git", "--work-tree", str(repo_path), "submodule", "update", "--init"]
        )
        for ext in self.extensions:
            self.build_extension(ext)

    def build_extension(self, ext):
        extdir = os.path.abspath(os.path.dirname(self.get_ext_fullpath(ext.name)))
        if not extdir.endswith(os.path.sep):
            extdir += os.path.sep
        # debug or release build flag for cmake
        cfg = "Debug" if os.environ.get("DEBUG_BUILD", "0") == "1" else "Release"
        cmake_args = [
            f"-DCMAKE_LIBRARY_OUTPUT_DIRECTORY={extdir}",
            f"-DPYTHON_EXECUTABLE={sys.executable}",
            f"-DCMAKE_BUILD_TYPE={cfg}"
        ]

        os.makedirs(self.build_temp, exist_ok=True)
        subprocess.check_call(
            ["cmake", ext.sourcedir] + cmake_args, cwd=self.build_temp
        )
        subprocess.check_call(
            ["cmake", "--build", ".", "--config", cfg, "--", f"-j{os.cpu_count()-1}"],
            cwd=self.build_temp,
        )


setup(
    name='myapp',
    version=__version__,
    description='CookieCutter Pybind Project for Python/C++',
    url='https://github.com/sahibdhanjal',
    maintainer='Sahib Dhanjal',
    zip_safe=False,
    ext_modules=[CMakeExtension("myapp_cmake")],
    package_data={'myapp':['./../VERSION']},
    cmdclass={"build_ext": CMakeBuild},
)
