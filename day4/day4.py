with open('day4/day4_input.txt', 'r') as input_file:
    data = [line.strip() for line in input_file.readlines()]

test_data = [
    "2-4,6-8",
    "2-3,4-5",
    "5-7,7-9",
    "2-8,3-7",
    "6-6,4-6",
    "2-6,4-8"
]

print("part1")

def any_contained(pair: str):
    a, b = pair.split(',')
    a1, a2 = map(int, a.split('-'))
    b1, b2 = map(int, b.split('-'))
    if (a1>=b1 and a2<=b2) or (b1>=a1 and b2<=a2):
        return True
    else:
        return False

def any_overlap(pair: str):
    a, b = pair.split(',')
    a1, a2 = map(int, a.split('-'))
    b1, b2 = map(int, b.split('-'))
    if ((a2 >= b1) and (a1 <= b2)) or ((b2 >= a1) and (b1 <= a2)):
        return True
    else:
        return False

test_total = 0
for pair in test_data:
    if any_contained(pair):
        test_total += 1

print(f"[TEST_DATA] Total pairs fully contained: {test_total}")

total = 0
for pair in data:
    if any_contained(pair):
        total += 1

print(f"Total pairs fully contained: {total}")

print("part 2")

test_total = 0
for pair in test_data:
    if any_overlap(pair):
        test_total += 1

print(f"[TEST_DATA] Total pairs overlapping: {test_total}")

total = 0
for pair in data:
    if any_overlap(pair):
        total += 1

print(f"Total pairs overlapping: {total}")