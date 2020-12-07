# CHAPTER 1
# The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day. "Something's wrong with our
# computers; we can't log in!" You ask if you can take a look. Their password database seems to be a little
# corrupted: some of the passwords wouldn't have been allowed by the Official Toboggan Corporate Policy that was in
# effect when they were chosen. To try to debug the problem, they have created a list (your puzzle input) of
# passwords (according to the corrupted database) and the corporate policy when that password was set. For example,
# suppose you have the following list:
# 1-3 a: abcde
# 1-3 b: cdefg
# 2-9 c: ccccccccc
# Each line gives the password policy
# and then the password. The password policy indicates the lowest and highest number of times a given letter must
# appear for the password to be valid. For example, 1-3 a means that the password must contain a at least 1 time and
# at most 3 times. In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains no
# instances of b, but needs at least 1. The first and third passwords are valid: they contain one a or nine c,
# both within the limits of their respective policies.
# How many passwords are valid according to their policies?

#--- Part Two ---

# While it appears you validated the passwords correctly, they don't seem to be what the Official Toboggan Corporate
# Authentication System is expecting. The shopkeeper suddenly realizes that he just accidentally explained the
# password policy rules from his old job at the sled rental place down the street! The Official Toboggan Corporate
# Policy actually works a little differently. Each policy actually describes two positions in the password,
# where 1 means the first character, 2 means the second character, and so on. (Be careful; Toboggan Corporate
# Policies have no concept of "index zero"!) Exactly one of these positions must contain the given letter. Other
# occurrences of the letter are irrelevant for the purposes of policy enforcement. Given the same example list from
# above: 1-3 a: abcde is valid: position 1 contains a and position 3 does not. 1-3 b: cdefg is invalid: neither
# position 1 nor position 3 contains b. 2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c. How
# many passwords are valid according to the new interpretation of the policies?


import re
#open the input
file = open("dec02.dat", mode="r")
#read input
pwList = file.readlines()
file.close()
# Part 1

# count Correct Passwords over the input
correctPW = 0

# each entry is a tuple of information
# for every entry you have to
for pwTuple in pwList:
    # split the front part and the back part into list entries
    pwTupleArray = pwTuple.split(": ")
    # the second entry in these list needs to get rid of the "newline"
    pwTupleArray[1] = pwTupleArray[1].rstrip("\n")
    # the first entry needs to be split into the three conditions
    pwCondArray = re.split('-| ', pwTupleArray[0])
    countChar = 0
    # the lowest amount of appearance of the searched character
    lowest = int(pwCondArray[0])
    # the highest amount
    highest = int(pwCondArray[1])
    # the character searched for
    searchChar = pwCondArray[2]
    # now count the searched char in the string
    for i in pwTupleArray[1]:
        if i == searchChar:
            countChar += 1
    # now check if this count ist between lowest and highest count
    if lowest <= countChar:
        if highest >= countChar:
            # if so count it
            correctPW += 1

print("Part 1: " + str(correctPW))

# Part 2

# count again
correctPWPart2 = 0

# the arrays above are potentiale filled with corrupted data
# so I build the stack again

# each entry is a tuple of information
# for every entry you have to
for pwTuple in pwList:
    # split the front part and the back part into list entries
    pwTupleArray = pwTuple.split(": ")
    # the conditions are stored in the first entry and needs to be split in a new list
    pwCondArray = re.split('-| ',pwTupleArray[0])
    # now its not low- and high-counts but targets in the array
    # -1 because of index 0
    firstTarget = int(pwCondArray[0])-1
    secondTarget = int(pwCondArray[1])-1
    searchChar = pwCondArray[2]

    # the entry in pwTupleArray[1] needs to be a list itself
    pw = list(pwTupleArray[1])
    # if there is ONLY ONE Target hit its valid
    if (pw[firstTarget] == searchChar) != (pw[secondTarget] == searchChar):
        correctPWPart2 += 1

print("Part 2: " + str(correctPWPart2))



