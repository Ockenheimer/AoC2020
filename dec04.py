# --- Day 4: Passport Processing ---
#
# You arrive at the airport only to realize that you grabbed your North Pole Credentials instead of your passport.
# While these documents are extremely similar, North Pole Credentials aren't issued by a country and therefore aren't
# actually valid documentation for travel in most of the world. It seems like you're not the only one having
# problems, though; a very long line has formed for the automatic passport scanners, and the delay could upset your
# travel itinerary. Due to some questionable network security, you realize you might be able to solve both of these
# problems at the same time. The automatic passport scanners are slow because they're having trouble detecting which
# passports have all required fields. The expected fields are as follows:
#
#     byr (Birth Year)
#     iyr (Issue Year)
#     eyr (Expiration Year)
#     hgt (Height)
#     hcl (Hair Color)
#     ecl (Eye Color)
#     pid (Passport ID)
#     cid (Country ID)
#
# Passport data is validated in batch files (your puzzle input). Each passport is represented as a sequence of
# key:value pairs separated by spaces or newlines. Passports are separated by blank lines. Here is an example batch
# file containing four passports:
#
# ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
# byr:1937 iyr:2017 cid:147 hgt:183cm
#
# iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
# hcl:#cfa07d byr:1929
#
# hcl:#ae17e1 iyr:2013
# eyr:2024
# ecl:brn pid:760753108 byr:1931
# hgt:179cm
#
# hcl:#cfa07d eyr:2025 pid:166559648
# iyr:2011 ecl:brn hgt:59in
#
# The first passport is valid - all eight fields are present. The second passport is invalid - it is missing hgt (the
# Height field). The third passport is interesting; the only missing field is cid, so it looks like data from North
# Pole Credentials, not a passport at all! Surely, nobody would mind if you made the system temporarily ignore
# missing cid fields. Treat this "passport" as valid. The fourth passport is missing two fields, cid and byr. Missing
# cid is fine, but missing any other field is not, so this passport is invalid. According to the above rules,
# your improved system would report 2 valid passports. Count the number of valid passports - those that have all
# required fields. Treat cid as optional. In your batch file, how many passports are valid?

def is_hex(s):
    try:
        int(s, 16)
        return True
    except ValueError:
        return False

# a counter for valid passwords
import re

pwCounter = 0

# open file
file = open("dec04.dat", mode="r")

# we need an assembled list to handle newLines
assembledList = []
# we need a string to build the list
newStr = ""

for line in file:
    if line != "\n":
        newStr += line.strip("\n").__add__(" ")
    else:
        assembledList += [newStr]
        newStr = ""

for entry in assembledList:

    # split the string in searchable entries in list
    analyseList = re.split(':| ', entry)
    if "byr" in analyseList and "iyr" in analyseList and "eyr" in analyseList and "hgt" in analyseList and "hcl" in analyseList and "ecl" in analyseList and "pid" in analyseList:
        byrValue = analyseList[analyseList.index("byr") + 1].rstrip(" ")
        iyrValue = analyseList[analyseList.index("iyr") + 1].rstrip(" ")
        eyrValue = analyseList[analyseList.index("eyr") + 1].rstrip(" ")
        hgtValue = analyseList[analyseList.index("hgt") + 1].rstrip(" ")
        hclValue = analyseList[analyseList.index("hcl") + 1].rstrip(" ")
        eclValue = analyseList[analyseList.index("ecl") + 1].rstrip(" ")
        pidValue = analyseList[analyseList.index("pid") + 1].rstrip(" ")
        # byr (Birth Year) - four digits; at least 1920 and at most 2002.
        if 1920 <= int(byrValue) <= 2002:
            # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
            if 2010 <= int(iyrValue) <= 2020:
                # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
                if 2020 <= int(eyrValue) <= 2030:
                    # hgt (Height) - a number followed by either cm or in:
                    if hgtValue[len(hgtValue) - 2: len(hgtValue)] == "cm" and 150 <= int(hgtValue[:-2]) <= 193 or hgtValue[len(hgtValue) - 2: len(hgtValue)] == "in" and 59 <= int(hgtValue[:-2]) <= 76:
                        # hcl(Hair Color) - a  # followed by exactly six characters 0-9 or a-f.
                        if hclValue[0] == "#" and is_hex(hclValue[1:]) and len(hclValue) == 7:
                            # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
                            if eclValue == "amb" or eclValue == "blu" or eclValue == "brn" or eclValue == "gry" or eclValue == "grn" or eclValue == "hzl" or eclValue == "oth":
                                # pid (Passport ID) - a nine-digit number, including leading zeroes.
                                if len(pidValue) == 9:
                                    pwCounter += 1

print(pwCounter)
