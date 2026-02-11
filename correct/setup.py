from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
import numpy
import os
import platform
import sys

BASENAME = 'correct'
NAME = 'lib' + BASENAME

NO_CUDA = os.environ.get("NO_CUDA") == "1"
libraries = [BASENAME, 'utils', 'm', 'pthread']
extra_compile_args = ['-fopenmp']
extra_link_args = ['-fopenmp']
library_dirs = ['lib', '../utils']
include_dirs = ['lib', '../utils', numpy.get_include()]

if platform.system() == "Darwin":
    env_lib = os.path.join(sys.prefix, 'lib')
    libraries.append('omp')
    extra_compile_args = ['-Xpreprocessor', '-fopenmp']
    extra_link_args = ['-L' + env_lib, '-Wl,-rpath,' + env_lib]
    library_dirs.append(env_lib)
else:
    libraries.append('gomp')

if not NO_CUDA:
    libraries.append('cudart')

extension = Extension(
    name=NAME,
    sources=[NAME + '.pyx'],
    libraries=libraries,
    language='c++',
    library_dirs=library_dirs,
    include_dirs=include_dirs,
    extra_compile_args=extra_compile_args,
    extra_link_args=extra_link_args,
)

setup(
    name=NAME,
    ext_modules=cythonize([extension]),
    version='0.1',
    description='Motion/shading correction for voltage imaging data'
)
