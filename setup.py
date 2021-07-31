from distutils.core import setup
from Cython.Build import cythonize
fileSet = set()
fileSet.add("app1/file1.py")
fileSet.add("app2/file2.py")
fileSet.add("app3/file3.py")
setup(
   ext_modules=cythonize(fileSet)
)
