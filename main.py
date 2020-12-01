
# Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input); apparently,
# something isn't quite adding up. Specifically, they need you to find the two entries that sum to 2020 and then
# multiply those two numbers together. For example, suppose your expense report contained the following:
# 1721 979 366 299 675 1456
# In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces
# 1721 * 299 = 514579, so the correct answer is 514579. Of course, your expense report is much larger. Find the two
# entries that sum to 2020; what do you get if you multiply them together?

#opening a file
file = open('inputDec01', mode='r')

#readlines gives a list of lines with "\n"
intList: list[str] = file.readlines()
#cleanup
file.close()

#for each line in the list
for x in intList:
    # numbers from striped strings
    x1 = int(x.rstrip("\n"))
    for y in intList:
        y1 = int(y.rstrip("\n"))
        #the maths
        if x1 + y1 == 2020:
            print(x1 * y1)
            exit()

