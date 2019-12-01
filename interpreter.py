import regex as re

file = "bfcode.txt"  # TODO allow input from cmd line not hardcoded

"""
BF reminder
< moves -1 along tape
> moves +1 along tape
+ add 1 to current cell
- sub 1 from current cell
[ jump to matching ] if current cell is 0
] jump back to matching [ if current cell is non zero
. output cell as ascii char
, take input and store ascii value
taken from https://esolangs.org/wiki/Brainfuck
"""

# read in file and strip out bad chars
with open("bfcode.txt", "r") as f:
    prog = f.read()
    prog = re.sub("[^<>\\+\\-\\[\\]\\.\\,]", "", prog)

memDict = dict()
# many places use a list for the memory however I believe a dict is more effective since:
# 1. you pay for the memory you use not the all the memory in between
# (while I accept Bf is a pretty memory light lang it never hurts to save space)
# 2. python has no trouble using ints as dict keys
# 3. the BF memory "tape" is now totally unbounded both positively and more importantly negatively, as intended
memPtr = 0  # pointer for memDict
progPtr = 0  # pointer for program

while progPtr < len(prog):
    if prog[progPtr] == "<":
        memPtr -= 1

    elif prog[progPtr] == ">":
        memPtr += 1

    elif prog[progPtr] == "+":
        memDict[memPtr] = memDict.get(memPtr, 0) + 1
        # get either returns a key's value if it exists or the default, 0 if not
        # this is our main mechanism for saving memory

    elif prog[progPtr] == "-":
        memDict[memPtr] = memDict.pop(memPtr, 0) - 1

    elif prog[progPtr] == ".":
        print(str(chr(memDict.get(memPtr, 0))), end="")

    elif prog[progPtr] == ",":
        memDict[memPtr] = ord(input("input:"))

    elif prog[progPtr] == "[":
        if memDict[memPtr] == 0:
            layers = 0
            while prog[progPtr] != "]" or layers != 0:
                progPtr += 1

    elif prog[progPtr] == "]":
        if memDict[memPtr] != 0:
            layers = 0
            while prog[progPtr] != "[" or layers != 0:
                progPtr -= 1

    progPtr += 1



