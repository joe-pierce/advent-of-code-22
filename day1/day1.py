with open('2022/day1_input.txt', 'r') as input_file:
    data = input_file.read()

test_data = "1000\n2000\n3000\n\n4000\n\n5000\n6000\n\n7000\n8000\n9000\n\n10000"

def get_elf_calories(data_input: str):
    parsed_data = [[int(itm) for itm in itms.split('\n')] for itms in data_input.split('\n\n')]
    sums = [sum(itms) for itms in parsed_data]
    return sums


# Part 1 - Max calories per elf
print(f"[TEST DATA] Max calories: {max(get_elf_calories(test_data))}")
print(f"Max calories: {max(get_elf_calories(data))}")

# Part 2 - Top 3 elves calories sum

test_top3_elf_calories =  sorted(get_elf_calories(test_data))[-3:]
top3_elf_calories =  sorted(get_elf_calories(data))[-3:]


print(f"[TEST DATA] Calories: {sum(test_top3_elf_calories)}")
print(f"Calories: {sum(top3_elf_calories)}")