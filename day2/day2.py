import math


def read_file(path):
    with open(path, 'r') as file:
        for line in file:
            yield [int(a) for a in line.strip().split()]


def check_if_safe(report):
    return sum(report) == math.copysign(1, report[0]) * sum([abs(b) for b in report]) and max([abs(b) for b in report]) < 4 and min([abs(b) for b in report]) > 0


def calculate_diff(report):
    res = []
    for i, v in enumerate(report):
        if i == len(report)-1:
            break
        res.append(v - report[i+1])
    return res


def get_subsets(report):
    result = set()

    for i in range(len(report)):
        new_lst = report[:i] + report[i+1:]
        result.add(tuple(new_lst))  # Convert to tuple to make it hashable

    return result


safe = 0
for report in read_file("data"):
    for i in get_subsets(report):
      if check_if_safe(calculate_diff(i)):
          safe += 1
          break
print(f"Number of safe reports: {safe}")
