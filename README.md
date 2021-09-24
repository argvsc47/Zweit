# Zweit
A build system for stuff with lots of files with the same compiler flags

# How to use

 - clone this repo and put `zweit.py` in your project root (or wherever you want, but be sure to update your PATH !)
 - write a zwscript file
 - and run zweit.py `your_zwscript_filename`

# File Format

 * The first line specifies the compiler (or interpreter) this is **mandatory**
 * the next non-empty line should specify the compiler flags, `-lstdc++` for example
 * the next following non-empty line should specify the source directory
 * and from there onwards all non-empty lines are the files to include
 * Additionally, you can make multiple commands that you can switch in between by adding a flag
 * to make a new command, you need to make a new line that starts with '#' and a space, and then the corresponding flag
 * from there you can specify the arguments for that command

Note that everything apart from the compiler and files can be omitted with `!NONE`   
Tip : if you want to pass '!' for flags per example, preceed it with a flag so `!X` becomes ` !X`

# Examples

build.zw (only default)
```
gcc
!NONE
src/

util.cpp
tools.cpp

main.cpp
```
in the terminal
```shell
zweit.py build.zw
```

build.zw (multiple commands)
```
gcc
!NONE
src/

util.cpp
tools.cpp
main.cpp

# -tests
gcc
-lstc++
tests/

test_1.cpp
test_2.cpp
test_3.cpp
```
in the terminal now, you can either run :
```shell
zweit.py build.zw
```
or :
```shell
zweit.py build.zw -tests
```
