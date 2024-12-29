import random

def monty_hall_simulation(num_trials, switch, num_doors, num_prizes):
  
    win_count = 0
    for _ in range(num_trials):
        # Initialize doors with one door containing the prize and the others empty
        doors = [0] * (num_doors - num_prizes) + [1] * (num_prizes) 
      
        # Choose random door
        player_door= random.randint(0, num_doors - 1)
      
        # Monty reveals door with a goat 
        remaining_doors = [i for i in range(num_doors) if i != player_door and doors[i] == 0]
        revealed_door = random.choice(remaining_doors)

        # If the player switches doors
        if switch:
            # Find the door to switch to 
            new_door = next(i for i in range(num_doors) if i != player_door and i != revealed_door)
            # Player switches to a random unchosen door 
            player_door = random.choice([i for i in range(num_doors) if i != player_door and i != new_door])

        # Check if the player won 
        if doors[player_door] == 1:
            win_count += 1
          
    return win_count

# Variables
num_trials = 10000
switch = True
num_doors = 4
num_prizes = 2

# Run
wins = monty_hall_simulation(num_trials, switch, num_doors, num_prizes)

# Calculate win % 
win_rate = wins / num_trials

print("Monty Hall Simulation Results:")
print(f"Number of Doors: {num_doors}")
print(f"Number of Prizes: {num_prizes}")
print(f"Strategy: {'Switch' if switch else 'Stay'}")
print(f"Number of Wins: {wins}")
print(f"Win %: {win_rate * 100:.2f} %")
