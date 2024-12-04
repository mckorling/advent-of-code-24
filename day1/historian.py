from collections import Counter

# take input and convert to left list and right list
file = open("/Users/megankorling/Developer/advent-of-code-24/day1/data.txt", "r")
left = []
right = []
for line in file:
    line = line.strip()
    values = line.split("   ")
    left.append(int(values[0]))
    right.append(int(values[1]))

# sort each list
# loop through list and find difference between the 2
# sum the differences
    
def calculate_diff_total(left, right):
    left.sort()
    right.sort()
    diff_total = 0
    
    for i in range(len(left)):
        diff = abs(left[i] - right[i])
        diff_total += diff
    
    return diff_total

test_left = [3, 4, 2, 1, 3, 3]
test_right = [4, 3, 5, 3, 9, 3]

# print(calculate_diff_total(test_left, test_right)) #11
# print(calculate_diff_total(left, right)) #1834060

# PART 2
# how often each number from left appears in the right
# multiply left number by how many times it is in right
# add up new left numbers

def calculate_similarities(left, right):
    right_count = Counter(right)
    total = 0

    for l in left:
        multiply_by = right_count.get(l, 0)
        total += l * multiply_by
    
    return total

print(calculate_similarities(test_left, test_right)) #31
print(calculate_similarities(left, right)) #21607792