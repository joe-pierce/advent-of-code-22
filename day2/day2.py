class RPS:
    def __init__(self, their_choice):
        self.choices = {
            'A': 'rock', 'B': 'paper', 'C': 'scissors', 
            'X': 'rock', 'Y': 'paper', 'Z': 'scissors'
        }
        self.results = {'X': 'lose', 'Y': 'draw', 'Z': 'win'}
        self.their_choice = self.choices[their_choice] if their_choice in self.choices else their_choice
        self.score = {'rock': 1, 'paper': 2, 'scissors': 3}
        self.beaten_by = {'rock': 'paper', 'paper': 'scissors', 'scissors': 'rock'}
        self.wins_against = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}

    
    def choose(self, my_choice) -> int:
        my_choice = self.choices[my_choice] if my_choice in self.choices else my_choice
        if (result := self.score[my_choice] - self.score[self.their_choice]) == 0:
            # draw
            return 3 + self.score[my_choice]
        elif result == 1 or result == -2:
            # win
            return 6 + self.score[my_choice]
        elif result == -1 or result == 2:
            # lose
            return self.score[my_choice]
    
    def result(self, result: str) -> str:
        result = self.results[result] if result in self.results else result
        if result == 'draw':
            return self.their_choice
        elif result == 'win':
            return self.beaten_by[self.their_choice]
        elif result == 'lose':
            return self.wins_against[self.their_choice]


score = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}

with open('day2/day2_input.txt', 'r') as input_file:
    data = input_file.readlines()

test_data = ['A Y', 'B X', 'C Z']


## PART 1
print("\nPart 1\n---------")

test_total = 0
for game in test_data:
    their_choice, my_choice = game.split()
    test_total += RPS(their_choice).choose(my_choice)

print(f"[TEST DATA] Total score: {test_total}")

total = 0
for game in data:
    their_choice, my_choice = game.split()
    total += RPS(their_choice).choose(my_choice)

print(f"Total score: {total}")

## PART 2 

print("\nPart 2\n---------")

# reset data so that x = lose, y = draw, z = win
test_total = 0
for game in test_data:
    their_choice, result = game.split()
    my_choice = RPS(their_choice).result(result)
    test_total += RPS(their_choice).choose(my_choice)

print(f"[TEST DATA] Total score: {test_total}")

total = 0
for game in data:
    their_choice, result = game.split()
    my_choice = RPS(their_choice).result(result)
    total += RPS(their_choice).choose(my_choice)

print(f"Total score: {total}")

