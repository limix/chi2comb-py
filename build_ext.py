import os
import platform
from os.path import join

from cffi import FFI

from libpath import Unix, Windows

ffibuilder = FFI()
libs = ["chi2comb"]

folder = os.path.dirname(os.path.abspath(__file__))

with open(join(folder, "chi2comb", "interface.h"), "r") as f:
    ffibuilder.cdef(f.read())

if platform.system() == "Windows":
    s = Windows()
    f = s.get_programfiles()
    for lib in libs:
        s.add_library_dir(join(f, lib, "lib"))
        s.add_include_dir(join(f, lib, "include"))

    libs = [s.find_libname(lib) for lib in libs]
else:
    s = Unix()

library_dirs = s.get_library_dirs()
extra_link_args = []
if platform.system() == "Darwin":
    if len(library_dirs) > 0:
        extra_link_args += ["-Wl,-rpath," + ",-rpath,".join(library_dirs)]

ffibuilder.set_source(
    "chi2comb._ffi",
    '#include "chi2comb.h"',
    libraries=libs,
    library_dirs=library_dirs,
    include_dirs=s.get_include_dirs(),
    extra_link_args=extra_link_args,
    language="c",
)

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
