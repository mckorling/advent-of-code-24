# each line is a report
# each number in a report is a level
# a safe report is 
    # only increasing or decreasing
    # and adjacent levels differ by 1 - 3 (inclusive)

# return the number of safe reports

file = open("/Users/megankorling/Developer/advent-of-code-24/day2/data.txt", "r")
reports = []
for line in file:
    line = line.strip()
    values = line.split(" ")
    numbers = [int(x) for x in values]
    reports.append(numbers)

# print(reports)
test_reports = [
    [7, 6, 4, 2, 1],
    [1, 2, 7, 8, 9],
    [9, 7, 6, 2, 1],
    [1, 3, 2, 4, 5],
    [8, 6, 4, 4, 1],
    [1, 3, 6, 7, 9]
]

def is_safe_report(report):
    if (len(report) == 1):
        return True
    
    if (report[0] == report[1]):
        return False

    is_desc = report[0] > report[1]
    # print(is_desc)
    for i in range(1, len(report)):
        prev = report[i-1]
        curr = report[i]
        if (is_desc and (prev - curr < 1 or prev - curr > 3)):
            return False
        if (not is_desc and (curr - prev < 1 or curr - prev > 3)):
            return False
        
    return True

def get_safe_reports(reports):
    total = 0
    for report in reports:
        is_safe = is_safe_report(report)
        if is_safe:
            total += 1

    return total

# print(get_safe_reports(test_reports)) # 2
# print(get_safe_reports(reports)) # 279

# PART 2
# 1 level can be removed from a report and be safe
def get_safe_reports_damp(reports):
    total = 0
    for report in reports:
        # print(report)
        is_safe = is_safe_report(report)
        if is_safe:
            total += 1
        else: 
            for i in range(len(report)):
                copy = [x for x in report]
                copy.pop(i) 
                # print(copy)
                if is_safe_report(copy):
                    total += 1
                    break
    return total

print(get_safe_reports_damp(test_reports)) # 4
print(get_safe_reports_damp(reports)) # 343