cmakew
========

.. image:: https://badge.fury.io/py/cmakew.svg
    :target: https://badge.fury.io/py/cmakew

.. image:: https://img.shields.io/pypi/pyversions/cmakew.svg
    :target: https://pypi.python.org/pypi/cmakew


Summary
-------

A CLI tool for CMake and compiler wrapper.


Examples
==========

Build googletest at Linux
--------------------------

.. code:: console

    $ cmakew googletest-release-1.8.0
    [INFO] cmakew: -- The C compiler identification is GNU 6.2.1
    -- The CXX compiler identification is GNU 6.2.1
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
    -- Found PythonInterp: /root/.pyenv/shims/python (found version "2.7.12")
    -- Looking for pthread.h
    -- Looking for pthread.h - found
    -- Looking for pthread_create
    -- Looking for pthread_create - not found
    -- Looking for pthread_create in pthreads
    -- Looking for pthread_create in pthreads - not found
    -- Looking for pthread_create in pthread
    -- Looking for pthread_create in pthread - found
    -- Found Threads: TRUE
    -- Configuring done
    -- Generating done
    -- Build files have been written to: /home/github/build

    [INFO] cmakew: Scanning dependencies of target gtest
    Scanning dependencies of target gmock
    Scanning dependencies of target gmock_main
    [  9%] Building CXX object googlemock/gtest/CMakeFiles/gtest.dir/src/gtest-all.cc.o
    [ 18%] Building CXX object googlemock/CMakeFiles/gmock.dir/src/gmock-all.cc.o
    [ 27%] Building CXX object googlemock/CMakeFiles/gmock.dir/__/googletest/src/gtest-all.cc.o
    [ 36%] Building CXX object googlemock/CMakeFiles/gmock_main.dir/__/googletest/src/gtest-all.cc.o
    [ 45%] Building CXX object googlemock/CMakeFiles/gmock_main.dir/src/gmock-all.cc.o
    [ 54%] Linking CXX static library libgtest.a
    [ 63%] Linking CXX static library libgmock.a
    [ 72%] Building CXX object googlemock/CMakeFiles/gmock_main.dir/src/gmock_main.cc.o
    [ 72%] Built target gtest
    Scanning dependencies of target gtest_main
    [ 72%] Built target gmock
    [ 81%] Building CXX object googlemock/gtest/CMakeFiles/gtest_main.dir/src/gtest_main.cc.o
    [ 90%] Linking CXX static library libgtest_main.a
    [ 90%] Built target gtest_main
    [100%] Linking CXX static library libgmock_main.a
    [100%] Built target gmock_main

Output
~~~~~~~~~~~~

.. code:: console

    $ # tree build/googlemock/ -L 2
    build/googlemock/
    ├── CMakeFiles
    │   ├── CMakeDirectoryInformation.cmake
    │   ├── gmock.dir
    │   ├── gmock_main.dir
    │   └── progress.marks
    ├── CTestTestfile.cmake
    ├── Makefile
    ├── cmake_install.cmake
    ├── gtest
    │   ├── CMakeFiles
    │   ├── CTestTestfile.cmake
    │   ├── Makefile
    │   ├── cmake_install.cmake
    │   ├── libgtest.a
    │   └── libgtest_main.a
    ├── libgmock.a
    └── libgmock_main.a

    5 directories, 12 files



Installation
============

.. code:: console

    pip install cmakew


cmakew help
========================

.. code:: console

    usage: cmakew [-h] [--build-dir BUILD_DIR]
                  [--action {cmake,recmake,clean,build,rebuild}]
                  [--cmake-options CMAKE_OPTIONS] [--build-type {Debug,Release}]
                  [--generator GENERATOR] [--debug | --quiet]
                  SOURCE_DIR_PATH

    A CLI tool for CMake and compiler wrapper.

    positional arguments:
      SOURCE_DIR_PATH       relative path to the source directory.

    optional arguments:
      -h, --help            show this help message and exit
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
                            generator that pass to cmake. default value will be
                            decided by execution platform: (a) if executed at
                            Windows and Visual Studio is installed in C: or D:
                            drive, cmakew will pass 'Visual Studio NN' as a
                            generator to cmake. (b) "Unix Makefiles" otherwise


Dependencies
============

Python 2.7+ or 3.3+

- `logbook <http://logbook.readthedocs.io/en/stable/>`__
- `six <https://pypi.python.org/pypi/six/>`__
- `subprocrunner <https://github.com/thombashi/subprocrunner>`__
- `typepy <https://github.com/thombashi/typepy>`__
