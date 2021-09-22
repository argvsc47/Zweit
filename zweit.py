from sys import argv, exit
from os import system
from colorama import init, Fore
from time import time

if len(argv) == 1:
	exit("Too few arguments")

with open(argv[1]) as f:
	lines = f.read().split("\n")

if len(lines) < 6:
	exit("Wrong formatted build file")

init()

COMPILER = lines[0]
FLAGS = lines[1]
SRC = lines[3]
FILES = []

for file in lines[5:]:
	FILES.append(file)

total = 0

print(f"Building {Fore.YELLOW}{argv[1]}{Fore.RESET}")

for file in FILES:
	print(f"- Compiling file: {file}, path: {SRC+file}")
	start = time()
	if system(f"{COMPILER} {SRC+file} {FLAGS}") != 0:
		print(f"* Compiling file: {Fore.RED}{file} FAILED{Fore.RESET}")
	else:
		end = time()
		print(f"+ File Compiled: {Fore.CYAN}{file}{Fore.RESET}, in: {Fore.GREEN}{end-start}s{Fore.RESET}")
		total += end-start

print(f"Built {Fore.YELLOW}{argv[1]}{Fore.RESET} in: {Fore.GREEN}{total}s{Fore.RESET}")