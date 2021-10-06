from sys import argv, exit
from os import system
from colorama import init, Fore
from time import time

if len(argv) == 1:
	exit("Too few arguments")

with open(argv[1]) as f:
	lns = f.read().split("\n")

init()

def make_command(lines):
	lidx = 0

	COMPILER = lines[0]
	lidx = 1

	while lines[lidx] == "":
		lidx += 1

	FLAGS = "" if lines[lidx] == "!NONE" else lines[lidx]
	lidx += 1

	while lines[lidx] == "":
		lidx += 1

	SRC = "" if lines[lidx] == "!NONE" else lines[lidx]
	lidx += 1

	while lines[lidx] == "":
		lidx += 1

	FILES = []

	for file in lines[lidx:]:
		if file == "":
			continue
		FILES.append(file)

	return {
		"compiler": COMPILER,
		"flags": FLAGS,
		"source": SRC,
		"files": FILES
	}

def build(cfg):
	COMPILER = cfg["compiler"]
	FLAGS = cfg["flags"]
	SRC = cfg["source"]
	FILES = cfg["files"]

	total = 0

	print(f"Building {Fore.YELLOW}{argv[1]}{Fore.RESET}")

	for file in FILES:
		print(f"- Compiling file: {file}, path: {SRC+file}")
		start = time()
		if system(f"{COMPILER} {SRC+file} {FLAGS}") != 0:
			end = time()
			print(f"* Compiling file: {Fore.RED}{file} FAILED{Fore.RESET}")
		else:
			end = time()
			print(f"+ File Compiled: {Fore.CYAN}{file}{Fore.RESET}, in: {Fore.GREEN}{end-start}s{Fore.RESET}")
		total += end-start

	print(f"Built {Fore.YELLOW}{argv[1]}{Fore.RESET} in: {Fore.GREEN}{total}s{Fore.RESET}")

data = []
NEW = False
offset = 0
name = "default"
batch = []

for _, ln in enumerate(lns):
	if ln.startswith("#"):
		if batch:
			data.append(
				[name, batch]
			)
		name = ln[2:]
		offset = _+1
		batch = []
		continue

	batch.append(ln)

if batch: #cleanup
	data.append([name, batch])

cmds = {}
for batch in data:
	cmds.update({batch[0]:make_command(batch[1])})

if len(argv) == 2:
	if "default" in cmds:
		build(cmds["default"])
	else:
		exit("No default option set.")
else:
	if argv[2] in cmds:
		build(cmds[argv[2]])
	else:
		exit(f"No {argv[2]} option set.")
