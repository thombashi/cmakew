.. contents:: **cmakew**
   :backlinks: top
   :local:


Summary
==========
cmakew is a CMake wrapper CLI tool.


.. image:: https://badge.fury.io/py/cmakew.svg
    :target: https://badge.fury.io/py/cmakew
    :alt: PyPI package version

.. image:: https://img.shields.io/pypi/pyversions/cmakew.svg
    :target: https://pypi.org/project/cmakew
    :alt: Supported Python versions


Examples
==========
Build googletest at Linux
--------------------------

.. code:: console

    $ wget -O - https://github.com/google/googletest/archive/release-1.8.1.tar.gz | tar zxf -
    $ cmakew googletest-release-1.8.1/
    [INFO] cmakew: -- The C compiler identification is GNU 7.3.0
    -- The CXX compiler identification is GNU 7.3.0
    -- Check for working C compiler: /usr/bin/cc
    -- Check for working C compiler: /usr/bin/cc -- works
    -- Detecting C compiler ABI info
    -- Detecting C compiler ABI info - done
    -- Detecting C compile features
    -- Detecting C compile features - done
    -- Check for working CXX compiler: /usr/bin/c++
    -- Check for working CXX compiler: /usr/bin/c++ -- works
    -- Detecting CXX compiler ABI info
    -- Detecting CXX compiler ABI info - done
    -- Detecting CXX compile features
    -- Detecting CXX compile features - done
    -- Found PythonInterp: /home/toor/.pyenv/versions/3.7.0/bin/python (found version "3.7")
    -- Looking for pthread.h
    -- Looking for pthread.h - found
    -- Looking for pthread_create
    -- Looking for pthread_create - not found
    -- Check if compiler accepts -pthread
    -- Check if compiler accepts -pthread - yes
    -- Found Threads: TRUE
    -- Configuring done
    -- Generating done
    -- Build files have been written to: /home/github/build

    [INFO] cmakew: Scanning dependencies of target gtest
    [ 12%] Building CXX object googlemock/gtest/CMakeFiles/gtest.dir/src/gtest-all.cc.o
    [ 25%] Linking CXX static library libgtestd.a
    [ 25%] Built target gtest
    Scanning dependencies of target gtest_main
    [ 37%] Building CXX object googlemock/gtest/CMakeFiles/gtest_main.dir/src/gtest_main.cc.o
    Scanning dependencies of target gmock
    [ 50%] Building CXX object googlemock/CMakeFiles/gmock.dir/src/gmock-all.cc.o
    [ 62%] Linking CXX static library libgtest_maind.a
    [ 62%] Built target gtest_main
    [ 75%] Linking CXX static library libgmockd.a
    [ 75%] Built target gmock
    Scanning dependencies of target gmock_main
    [ 87%] Building CXX object googlemock/CMakeFiles/gmock_main.dir/src/gmock_main.cc.o
    [100%] Linking CXX static library libgmock_maind.a
    [100%] Built target gmock_main


Output
~~~~~~~~~~~~
.. code:: console

    $ tree build/googlemock/ -L 2
    build/googlemock/
    ├── CMakeFiles
    │   ├── CMakeDirectoryInformation.cmake
    │   ├── gmock.dir
    │   ├── gmock_main.dir
    │   └── progress.marks
    ├── cmake_install.cmake
    ├── CTestTestfile.cmake
    ├── gtest
    │   ├── CMakeFiles
    │   ├── cmake_install.cmake
    │   ├── CTestTestfile.cmake
    │   ├── generated
    │   ├── libgtestd.a
    │   ├── libgtest_maind.a
    │   └── Makefile
    ├── libgmockd.a
    ├── libgmock_maind.a
    └── Makefile

    6 directories, 12 files


Installation
============
.. code:: console

    pip install cmakew


cmakew help
========================
.. code:: console

    usage: cmakew [-h] [-V] [--build-dir BUILD_DIR]
                  [--action {cmake,recmake,clean,build,rebuild}]
                  [--cmake-options CMAKE_OPTIONS] [--build-type {Debug,Release}]
                  [--generator GENERATOR] [--debug | --quiet]
                  SOURCE_DIR_PATH

    A CLI tool for CMake and compiler wrapper.

    positional arguments:
      SOURCE_DIR_PATH       relative path to the source directory.

    optional arguments:
      -h, --help            show this help message and exit
      -V, --version         show program's version number and exit
      --debug               for debug print.
      --quiet               suppress execution log messages.

    Directory Options:
      --build-dir BUILD_DIR
                            relative path to the build output directory (defaults
                            to 'build').

    Build Options:
      --action {cmake,recmake,clean,build,rebuild}
                            cmake: execute CMake and exit. clean: delete existing
                            build directory and exit. recmake: delete existing
                            CMakeCache and execute CMake after that. build:
                            execute MSBuild to Visual Studio solution files that
                            created by cmake. rebuild: delete existing build
                            directory and execute CMake and MSBuild after that.
                            defaults to 'build'.

    CMake Options:
      --cmake-options CMAKE_OPTIONS
                            path to the CMake options file. use "{key :value,
                            ...}" to set specific parameters. defaults to
                            cmake_options.json.
      --build-type {Debug,Release}
                            defaults to Debug.
      --generator GENERATOR
                            generator that passes to cmake. the default value
                            decided by execution platform: (a) if executed at
                            Windows and Visual Studio is installed in C: or D:
                            drive, cmakew pass 'Visual Studio NN' as a generator
                            to cmake. (b) "Unix Makefiles" otherwise

    Issue tracker: https://github.com/thombashi/cmakew/issues


Dependencies
============
Python 2.7+ or 3.4+

- `logbook <https://logbook.readthedocs.io/en/stable/>`__
- `six <https://pypi.org/project/six/>`__
- `subprocrunner <https://github.com/thombashi/subprocrunner>`__
- `typepy <https://github.com/thombashi/typepy>`__
