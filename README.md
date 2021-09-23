# Zweit
A build system for stuff with lots of files with the same compiler flags

# How to use

 - clone this repo and put `zweit.py` in your project root (or wherever you want)
 - write a zwscript file
 - and run zweit.py `your_zwscriptfile_name`

# File Format

```
// first line is for the compiler name (MANDATORY
// second line is for the compiler flags (or type !NONE if there isn't any)
// third line is the source dir (where your files are, or put !NONE if there isn't any)
// from the fourth line and onwards are the files names

```

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
in terminal
```
zweit.py build.zw
```
