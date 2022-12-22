with open('day7/day7_input.txt', 'r') as input_file:
    data = [line.strip() for line in input_file.readlines()]

test_data = [
    "$ cd /",
    "$ ls",
    "dir a",
    "14848514 b.txt",
    "8504156 c.dat",
    "dir d",
    "$ cd a",
    "$ ls",
    "dir e",
    "29116 f",
    "2557 g",
    "62596 h.lst",
    "$ cd e",
    "$ ls",
    "584 i",
    "$ cd ..",
    "$ cd ..",
    "$ cd d",
    "$ ls",
    "4060174 j",
    "8033020 d.log",
    "5626152 d.ext",
    "7214296 k"
]

class Tree:
    def __init__(self, data: list[str]):
        self.input = data
        self.dirs = {'/': 0}
        self.current_dir_path = '/'
        self.counted_files = set()
        self.parse_input()
        self.update_dir_sizes()

    def parse_input(self):
        for line in self.input:
            if line.startswith('$'):
                self.handle_action(line)
            else:
                self.handle_data(line)
    
    def move_up(self):
        idx = self.current_dir_path.rfind('/')
        self.current_dir_path = self.current_dir_path[:idx]
    
    def handle_action(self, line: str):
        if line == '$ ls':
            return # no action needed
        new_dir = line.partition('$ cd ')[2]

        if new_dir == '..': self.move_up()
        elif new_dir == '/': self.current_dir_path = '/'
        else: self.current_dir_path = self.current_dir_path + '/' + new_dir
    
    def handle_data(self, line: str):
        start, _, name = line.partition(' ')
        if start == 'dir':
            if self.current_dir_path + '/' + name not in self.dirs:
                self.dirs[self.current_dir_path + '/' + name] = 0
        else:
            if self.current_dir_path + '/' + name not in self.counted_files:
                self.dirs[self.current_dir_path] += int(start)
                self.counted_files.add(self.current_dir_path+ '/' + name)

    def update_dir_sizes(self):
        all_dir_paths = self.dirs.keys()
        longest_path = max(map(lambda x: x.count('/'), all_dir_paths))
        path_length = longest_path
        while path_length > 0:
            for _dir in self.dirs:
                if _dir.count('/') == path_length:
                    inner_dirs = filter(lambda x: _dir == x[:x.rfind('/')], self.dirs.keys())
                    self.dirs[_dir] += sum(self.dirs[inner_dir] for inner_dir in inner_dirs)
            path_length -= 1

    def sum_of_dirs_sub_100k(self):
        total = 0
        for dir, size in self.dirs.items():
            if size <= 100000:
                total += size

        return total

    def smallest_dir_bigger_than(self, size):
        smallest_suitable_dir = self.dirs['/']
        for _dir, dir_size in self.dirs.items():
            if dir_size > size:
                if dir_size < smallest_suitable_dir:
                    smallest_suitable_dir = dir_size

        return smallest_suitable_dir


print("Part 1")
test_tree = Tree(test_data)
print(f"[TEST DATA] Size of sub 100k folders: {test_tree.sum_of_dirs_sub_100k()}")

tree = Tree(data)
print(f"Size of sub 100k folders: {tree.sum_of_dirs_sub_100k()}")
    
print("Part 2")
TOTAL_SPACE = 70000000
SPACE_NEEDED = 30000000

space_available = TOTAL_SPACE - test_tree.dirs['/']
to_delete = SPACE_NEEDED - space_available
print(f"Smallest suitable dir size: {test_tree.smallest_dir_bigger_than(to_delete)}")

space_available = TOTAL_SPACE - tree.dirs['/']
to_delete = SPACE_NEEDED - space_available
print(f"Smallest suitable dir size: {tree.smallest_dir_bigger_than(to_delete)}")