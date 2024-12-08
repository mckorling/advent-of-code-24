# words can be horizontal, vertical, diagonal
# forwards or backwards, and can reuse letters from other words
# return how many times it appears in puzzle

# example, with answer below
# MMMSXXMASM
# MSAMXMSMSA
# AMXSXMAAMM
# MSAMASMSMX
# XMASAMXAMM
# XXAMMXXAMA
# SMSMSASXSS
# SAXAMASAAA
# MAMMMXMMMM
# MXMXAXMASX

# 18 times
# ....XXMAS.
# .SAMXMS...
# ...S..A...
# ..A.A.MS.X
# XMASAMX.MM
# X.....XA.A
# S.S.S.S.SS
# .A.A.A.A.A
# ..M.M.M.MM
# .X.X.XMASX

file = open("/Users/megankorling/Developer/advent-of-code-24/day4/data.txt", "r")
data = []
for line in file:
    line = line.strip()
    data.append([x for x in line])

test_data = [
    ['M','M','M','S','X','X','M','A','S','M'], # 0
    ['M','S','A','M','X','M','S','M','S','A'], # 1
    ['A','M','X','S','X','M','A','A','M','M'], # 2
    ['M','S','A','M','A','S','M','S','M','X'], # 3
    ['X','M','A','S','A','M','X','A','M','M'], # 4
    ['X','X','A','M','M','X','X','A','M','A'], # 5
    ['S','M','S','M','S','A','S','X','S','S'], # 6
    ['S','A','X','A','M','A','S','A','A','A'], # 7
    ['M','A','M','M','M','X','M','M','M','M'], # 8
    ['M','X','M','X','A','X','M','A','S','X']  # 9
]

# loop through each line
# loop through each letter
# if an x is found, call helper method
# add result to a running total count
def word_search(data, value):
    x_total = 0
    m_total = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == 'X':
                x_total += count_xmas(data, i, j)
            if data[i][j] == 'M':
                m_total += count_mas(data, i, j)

    if value == 'X':
        return x_total
    else:
        return m_total / 2


# helper method takes the full data, and i, j 
# it will check in the four directions if xmas is spelled
# returns count 
def count_xmas(data, i, j):
    total = 0
    col_bound = len(data)
    row_bound = len(data[0])
    within_upper_bound = i - 3 >= 0
    within_lower_bound = i + 3 < col_bound
    within_right_bound = j + 3 < row_bound
    within_left_bound = j - 3 >= 0
    # check up
    if (within_upper_bound):
        if data[i][j] + data[i-1][j] + data[i-2][j] + data[i-3][j] == 'XMAS':
            total += 1
    # check left
    if (within_left_bound):
        if data[i][j] + data[i][j-1] + data[i][j-2] + data[i][j-3] == 'XMAS':
            total += 1
    # check right
    if (within_right_bound):
        if data[i][j] + data[i][j+1] + data[i][j+2] + data[i][j+3] == 'XMAS':
            total += 1
    # check down
    if (within_lower_bound):
        if data[i][j] + data[i+1][j] + data[i+2][j] + data[i+3][j] == 'XMAS':
            total += 1
    # check diagonal top right
    if (within_upper_bound and within_right_bound):
        if data[i][j] + data[i-1][j+1] + data[i-2][j+2] + data[i-3][j+3] == 'XMAS':
            total += 1
    # check diagonal bottom right
    if (within_lower_bound and within_right_bound):
        if data[i][j] + data[i+1][j+1] + data[i+2][j+2] + data[i+3][j+3] == 'XMAS':
            total += 1
    # check diagonal bottom left
    if (within_lower_bound and within_left_bound):
        if data[i][j] + data[i+1][j-1] + data[i+2][j-2] + data[i+3][j-3] == 'XMAS':
            total += 1
    # check top left
    if (within_upper_bound and within_left_bound):
        if data[i][j] + data[i-1][j-1] + data[i-2][j-2] + data[i-3][j-3] == 'XMAS':
            total += 1
    # print('X at', i, j, 'total', total)
    return total

# print(word_search(test_data)) # 18
# print(word_search(data, 'X')) # 2414

# PART 2
# count where two MAS MAS intersect diagonally at A, can be backwards or forwards
# look for an m
# check diagonal bounds
# if mas is spelled, check the other direction
# add to total if it is correct
# not deduped at end, so divide by 2 for answer
def count_mas(data, i, j):
    total = 0
    col_bound = len(data)
    row_bound = len(data[0])
    within_upper_bound = i - 2 >= 0
    within_lower_bound = i + 2 < col_bound
    within_right_bound = j + 2 < row_bound
    within_left_bound = j - 2 >= 0
    # top right
    if (within_upper_bound and within_right_bound):
        word = data[i][j] + data[i-1][j+1] + data[i-2][j+2]
        cross_word = data[i][j+2] + data[i-1][j+1] + data[i-2][j]
        if word == 'MAS' and (cross_word == 'MAS' or cross_word == 'SAM'):
            total += 1
    # bottom right
    if (within_lower_bound and within_right_bound):
        word = data[i][j] + data[i+1][j+1] + data[i+2][j+2]
        cross_word = data[i][j+2] + data[i+1][j+1] + data[i+2][j]
        if word == 'MAS' and (cross_word == 'MAS' or cross_word == 'SAM'):            
            total += 1
    # bottom left
    if (within_lower_bound and within_left_bound):
        word = data[i][j] + data[i+1][j-1] + data[i+2][j-2]
        cross_word = data[i][j-2] + data[i+1][j-1] + data[i+2][j]
        if word == 'MAS' and (cross_word == 'MAS' or cross_word == 'SAM'):
            total += 1
    # top left
    if (within_upper_bound and within_left_bound):
        word = data[i][j] + data[i-1][j-1] + data[i-2][j-2]
        cross_word = data[i][j-2] + data[i-1][j-1] + data[i-2][j]
        if word == 'MAS' and (cross_word == 'MAS' or cross_word == 'SAM'):
            total += 1

    # if total > 0: print(i, j, total)
    return total

print(word_search(test_data, 'M'))
print(word_search(data, 'M')) # 1871