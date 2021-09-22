# Zweit
A build system for stuff with lots of files with the same compiler flags

# How to use

 - clone this repo and put `zweit.py` in your project root (or wherever you want)
 - write a zwscript file
 - and run zweit.py `your_zwscriptfile_name`

# File Format

```
// first line is for the compiler name
// second line is for the compiler flags (or leave blank if none)
// leave the third line empty
// fourth line is the source dir (where your files are)
// leave the fifth line empty
// from the sixth line and forward are the files names

```

# Examples

build.zw
```
gcc
-lstc++

src/

util.cpp
tools.cpp
main.cpp
```
```
zweit.py build.zw
```
