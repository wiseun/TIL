Install for google test
=======================

#### 1. Download
    1. Visit at [GoogleTest github](https://github.com/google/googletest).
    2. Download from [Git](https://github.com/google/googletest.git or zip file).

#### 2. Make source code
    1. Official method for google test is include by static library at your project.
    2. Go to ./googletest/googletest/scripts at your pc.
    3. python fuse_gtest_files.py $(your project path)
    4. Please check $(your project path)/gtest
    5. If you need main api for unit test, please copy ./googletest/googletest/src/gtest_main.cc to your project.

#### 3. Make static library and include at your unit test project.   

