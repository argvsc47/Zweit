# Zweit
A build system for stuff with lots of files with the same compiler flags

# How to use

 - clone this repo and put `zweit.py` in your project root (or wherever you want)
 - write a zwscript file
 - and run zweit.py `your_zwscript_filename`

# File Format

 * The first line specifies the compiler (or interpreter) this is **mandatory**
 * the next non-empty line should specify the compiler flags, `-lstdc++` for example
 * the next following non-empty line should specify the source directory
 * and from there onwards all non-empty lines are the files to include

Note that everything apart from the compiler and files can be omitted with `!NONE`

# Examples

build.zw
```
gcc
!NONE
src/

util.cpp
tools.cpp

main.cpp
```
in the terminal
```
zweit.py build.zw
```
