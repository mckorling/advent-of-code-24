import re

# take in file as one string
file = open("/Users/megankorling/Developer/advent-of-code-24/day3/data.txt", "r")
data = ""
print(data)
for line in file:
    line = line.strip()
    data += line

# find all places that fit mul(xyz, xyz)
# where xyz could be x, xy, or xyz
# multiply numbers
# add them to a running total
def multiply(mul):
    start_index = 4
    end_index = -1
    numbers = mul[start_index:end_index].split(",")
    return int(numbers[0]) * int(numbers[1])

# print(multiply("mul(11,8)"))

def get_total(data):
    matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)", data)
    total = 0
    print(matches)
    for match in matches:
        total += multiply(match)
    return total

test_data = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
# print(get_total(test_data)) # 161
# print(get_total(data)) # 179571322


# PART 2
# do() enables future mul instructions
# don't() disables future mul instructions
# the most recent instruction applies
# it is enabled at the beginning

test_data2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
def get_total_enabled(data):
    matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", data)
    is_enabled = True
    total = 0
    for match in matches:
        if match == 'do()':
            is_enabled = True
        elif match == "don't()":
            is_enabled = False
        else:
            if is_enabled:
                total += multiply(match)
    return total

print(get_total_enabled(test_data2)) # 48
print(get_total_enabled(data)) # 103811193