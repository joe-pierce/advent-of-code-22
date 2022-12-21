import string

item_priorities = {
    letter: score+1 for score, letter in enumerate(string.ascii_letters)
}

with open('day3/day3_input.txt', 'r') as input_file:
    data = input_file.readlines()

print("Part 1")

def get_common_item(backpack: str):
    backpack = backpack.strip()
    comp_size = int(len(backpack)/2)
    comp1 = set(backpack[:comp_size])
    comp2 = set(backpack[comp_size:])
    return list(comp1.intersection(comp2))[0]

test_data = [
    "vJrwpWtwJgWrhcsFMMfFFhFp",
    "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
    "PmmdzqPrVvPwwTWBwg",
    "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
    "ttgJtRGJQctTZtZT",
    "CrZsJsPPZsGzwwsLwLmpwMDw"
]

test_total = 0
for backpack in test_data:
    test_total += item_priorities[get_common_item(backpack)]

print(f"[TEST DATA] Total: {test_total}")

total = 0
for backpack in data:
    total += item_priorities[get_common_item(backpack)]

print(f"Total: {total}")

print("part 2")

def get_badge(backpacks: list[str]):
    b1, b2, b3 = [b.strip() for b in backpacks]
    return list(set(b1).intersection(b2).intersection(b3))[0]

# iterate in groups of three
test_total = 0
for i in range(0, len(test_data), 3):
    badge = get_badge(test_data[i:i+3])
    test_total += item_priorities[badge]

print(f"[TEST DATA] Total: {test_total}") 

# iterate in groups of three
total = 0
for i in range(0, len(data), 3):
    badge = get_badge(data[i:i+3])
    total += item_priorities[badge]

print(f"Total: {total}") 



