import regex as re

file = "bfcode.txt"  # TODO allow input from cmd line not hardcoded

"""
BF reminder
< moves -1 along tape
> moves +1 along tape
+ add 1 to current cell
- sub 1 from current cell
[ jump to matching ] if current cell is not 0
] jump back to matching [ if current cell is non zero
. output cell as ascii char
, take input and store ascii value
"""

# read in file and strip out bad chars
with open("bfcode.txt", "r") as f:
    prog = f.read()
    prog = re.sub("[^<>\\+\\-\\[\\]\\.\\,]", "", prog)





