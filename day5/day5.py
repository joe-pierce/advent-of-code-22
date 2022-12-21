with open('day5/day5_input.txt', 'r') as input_file:
    data = input_file.read()

test_data = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

class Stack:
    def __init__(self, raw_data: str) -> None:
        self.raw_stack, self.raw_moves = raw_data.split('\n\n')

        self.parse_stack()
        self.parse_moves()
        self.current_move = 0
    
    def parse_stack(self):
        self.columns = {int(col): [] for col in self.raw_stack.split('\n')[-1].split()}
        for row in self.raw_stack.split('\n')[:-1]:
            items = [row[i:i+3].strip('[] ') for i in range(0, len(row), 4)]
            for idx, item in enumerate(items):
                if item != '':
                    self.columns[idx+1].append(item)


    def parse_moves(self):
        moves = self.raw_moves.split('\n')
        moves = [
            (
                txt.replace('move', '')
                .replace('from', '')
                .replace('to', '')
                .strip()
                .split()
            ) for txt in moves
        ]
        self.moves = [[int(i) for i in move] for move in moves]

    def do_next_move(self):
        move = self.moves[self.current_move]
        for i in range(move[0]):
            block = self.columns[move[1]][0]
            self.columns[move[1]] = self.columns[move[1]][1:]
            self.columns[move[2]].insert(0, block)

        self.current_move += 1

    def do_all_moves(self):
        while self.current_move < len(self.moves):
            self.do_next_move()
    
    def do_next_move_9001(self):
        move = self.moves[self.current_move]
        
        blocks = self.columns[move[1]][:move[0]]
        self.columns[move[1]] = self.columns[move[1]][move[0]:]
        self.columns[move[2]] = blocks + self.columns[move[2]]

        self.current_move += 1

    def do_all_moves_9001(self):
        while self.current_move < len(self.moves):
            self.do_next_move_9001()

    def top_containers(self):
        string = ''
        for col, stack in self.columns.items():
            string += stack[0]
        return string

print("Part 1")

test_stack = Stack(test_data)
test_stack.do_all_moves()
print(f"[TEST DATA] Top containers are: {test_stack.top_containers()}")

stack = Stack(data)
stack.do_all_moves()
print(f"Top containers are: {stack.top_containers()}")

print("part 2")

test_stack = Stack(test_data)
test_stack.do_all_moves_9001()
print(f"[TEST DATA] Top containers (9001) are: {test_stack.top_containers()}")

stack = Stack(data)
stack.do_all_moves_9001()
print(f"Top containers (9001) are: {stack.top_containers()}")