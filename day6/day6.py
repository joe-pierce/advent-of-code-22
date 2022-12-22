with open('day6/day6_input.txt', 'r') as input_file:
    data = input_file.read()

test_datas = [
    "mjqjpqmgbljsphdztnvjfqwrcgsmlb",
    "bvwbjplbgvbhsrlpgdmjqwftvncz",
    "nppdvjthqldpwncqszvftbrmjlhg",
    "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",
    "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
]

def find_start_of_packet(data: str) -> int:
    for i in range(len(data)):
        substring = data[i:i+4]
        if len(set(substring)) == 4:
            return i+4

def find_start_of_message(data: str) -> int:
    for i in range(len(data)):
        substring = data[i:i+14]
        if len(set(substring)) == 14:
            return i+14

print("Part 1")
for test_data in test_datas:
    print(f"[TEST DATA] start of packet marker: {find_start_of_packet(test_data)}")

print(f"Start of packet marker: {find_start_of_packet(data)}")

print("Part 2")
for test_data in test_datas:
    print(f"[TEST DATA] start of packet marker: {find_start_of_message(test_data)}")

print(f"Start of packet marker: {find_start_of_message(data)}")

