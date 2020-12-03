# --- Day 3: Toboggan Trajectory ---
# Part 1
# With the toboggan login problems resolved, you set off toward the
# airport. While travel by toboggan might be easy, it's certainly not safe: there's very minimal steering and the
# area is covered in trees. You'll need to see which angles will take you near the fewest trees. # Due to the local
# geology, trees in this area only grow on exact integer coordinates in a grid. You make a map (your puzzle input) of
# the open squares (.) and trees (#) you can see. For example:
#
# ..##.......
# #...#...#..
# .#....#..#.
# ..#.#...#.#
# .#...##..#.
# ..#.##.....
# .#.#.#....#
# .#........#
# #.##...#...
# #...##....#
# .#..#...#.#
#
# These aren't the only trees, though; due to something you read about once involving arboreal genetics and biome
# stability, the same pattern repeats to the right many times:
#
# ..##.........##.........##.........##.........##.........##.......  --->
# #...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
# .#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
# ..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
# .#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
# ..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....  --->
# .#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
# .#........#.#........#.#........#.#........#.#........#.#........#
# #.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...
# #...##....##...##....##...##....##...##....##...##....##...##....#
# .#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#  --->
#
# You start on the open square (.) in the top-left corner and need to reach the bottom (below the bottom-most row on
# your map). The toboggan can only follow a few specific slopes (you opted for a cheaper model that prefers rational
# numbers); start by counting all the trees you would encounter for the slope right 3, down 1: From your starting
# position at the top-left, check the position that is right 3 and down 1. Then, check the position that is right 3
# and down 1 from there, and so on until you go past the bottom of the map. The locations you'd check in the above
# example are marked here with O where there was an open square and X where there was a tree:
#
# ..##.........##.........##.........##.........##.........##.......  --->
# #..O#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
# .#....X..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
# ..#.#...#O#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
# .#...##..#..X...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
# ..#.##.......#.X#.......#.##.......#.##.......#.##.......#.##.....  --->
# .#.#.#....#.#.#.#.O..#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
# .#........#.#........X.#........#.#........#.#........#.#........#
# #.##...#...#.##...#...#.X#...#...#.##...#...#.##...#...#.##...#...
# #...##....##...##....##...#X....##...##....##...##....##...##....#
# .#..#...#.#.#..#...#.#.#..#...X.#.#..#...#.#.#..#...#.#.#..#...#.#  --->
#
# In this example, traversing the map using this slope would cause you to encounter 7 trees. Starting at the top-left
# corner of your map and following a slope of right 3 and down 1, how many trees would you encounter?
#
# Part2
# Time to check the rest of the slopes - you need to minimize the probability of a sudden arboreal stop, after all.
# # Determine the number of trees you would encounter if, for each of the following slopes, you start at the top-left
# corner and traverse the map all the way to the bottom:
#
#     Right 1, down 1.
#     Right 3, down 1. (This is the slope you already checked.)
#     Right 5, down 1.
#     Right 7, down 1.
#     Right 1, down 2.
#
# In the above example, these slopes would find 2, 7, 3, 4, and 2 tree(s) respectively; multiplied together,
# these produce the answer 336.
# What do you get if you multiply together the number of trees encountered on each of the listed slopes?


# opening a file
file = open('dec03.dat', mode='r')

# Part 1: variables for the character in line and counting trees
# Part 2: also for the four other sleds
# sled E needs a line counter, because only every second line is counted
chrIntA = 0
chrIntB = 0
chrIntC = 0
chrIntD = 0
chrIntE = 0

lineE = 1

countTreeA = 0
countTreeB = 0
countTreeC = 0
countTreeD = 0
countTreeE = 0

# for each line in the file
for line in file:
    # split the line-string in characters
    lineArray = list(line)
    # count the #trees
    if lineArray[chrIntA] == "#":
        countTreeA += 1

    if lineArray[chrIntB] == "#":
        countTreeB += 1

    if lineArray[chrIntC] == "#":
        countTreeC += 1

    if lineArray[chrIntD] == "#":
        countTreeD += 1
    # count the trees only in uneven lines
    if lineE % 2 == 1:
        if lineArray[chrIntE] == "#":
            countTreeE += 1

    # count up the search index
    # there are 31 chr in each line so if the int is higher than 30 (index 0) than subtract 31
    chrIntA += 1
    if chrIntA > 30:
        chrIntA -= 31

    chrIntB += 3
    if chrIntB > 30:
        chrIntB -= 31

    chrIntC += 5
    if chrIntC > 30:
        chrIntC -= 31

    chrIntD += 7
    if chrIntD > 30:
        chrIntD -= 31
    # like counting trees, the search index is also counted up, if the line is uneven
    if lineE % 2 == 1:
        chrIntE += 1
        if chrIntE > 30:
            chrIntE -= 31

    lineE += 1

# multiply multiply
print(countTreeA * countTreeB * countTreeC * countTreeD * countTreeE)