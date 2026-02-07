from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
import numpy
import os

BASENAME = 'correct'
NAME = 'lib' + BASENAME

NO_CUDA = os.environ.get("NO_CUDA") == "1"
libraries = [BASENAME, 'utils', 'm', 'pthread', 'gomp']
if not NO_CUDA:
    libraries.append('cudart')

extension = Extension(
    name=NAME,
    sources=[NAME + '.pyx'],
    libraries=libraries,
    language='c++',
    library_dirs=['lib', '../utils'],
    include_dirs=['lib', '../utils', numpy.get_include()],
    extra_compile_args=['-fopenmp'],
    extra_link_args=['-fopenmp'],
)

setup(
    name=NAME,
    ext_modules=cythonize([extension]),
    version='0.1',
    description='Motion/shading correction for voltage imaging data'
)

