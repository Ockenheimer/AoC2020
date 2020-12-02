# CHAPTER 1
# Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input); apparently,
# something isn't quite adding up. Specifically, they need you to find the two entries that sum to 2020 and then
# multiply those two numbers together. For example, suppose your expense report contained the following:
# 1721 979 366 299 675 1456
# In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces
# 1721 * 299 = 514579, so the correct answer is 514579. Of course, your expense report is much larger. Find the two
# entries that sum to 2020; what do you get if you multiply them together?

# CHAPTER 2
# They offer you a second one if you can find three numbers in your expense report that meet the same
# criteria. Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them
# together produces the answer, 241861950. In your expense report, what is the product of the three entries that sum
# to 2020?

# opening a file
file = open('dec01.dat', mode='r')

# readlines() gives a list of lines with "\n"
intList: list[str] = file.readlines()
for entry in intList:
    intList[intList.index(entry)] = entry.strip('\n')
# cleanup
file.close()

# for each line in the list
for x in intList:
    x1 = int(x)
    # numbers from striped strings
    for y in intList[intList.index(x)+1:]:
        y1 = int(y)
        # chapter 2 addition
        for z in intList[intList.index(y)+1:]:
            z1 = int(z)
            # the maths
            if x1 + y1 + z1 == 2020:
                print("x = " + x + "; y = " + y + "; z = " + z)
                print(x1 * y1 * z1)

