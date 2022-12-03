# %%
from pathlib import Path
import numpy as np
# %% Loading input
with open(Path(__file__).parent / "input.txt", "r") as fh:
    input_data = fh.read()
input_data_flat = input_data.split("\n")

# %% Rule maps
shape_points = {
    "A": 1,  # Rock
    "B": 2,  # Paper
    "C": 3,  # Scissors
}

outcome_points = {
    "loss": 0,
    "draw": 3,
    "win": 6,
}

win_lookup = {
    "A": "C",  # Rock beats scissors
    "B": "A",  # Paper beats rock
    "C": "B",  # Scissors beat paper
}

loss_lookup = {
    "A": "B",  # Rock loses to paper
    "B": "C",  # Paper loses to scissors
    "C": "A",  # Scissors lose to rock
}

shape_to_presumed = {
    "A": "X",
    "B": "Y",
    "C": "Z",
}

presumed_to_shape = {v:k for k, v in shape_to_presumed.items()}

# %% Part 1: Score according to guide
points = 0

def get_outcome_from_entries(opponent_entry, my_entry):
    if (win_lookup[my_entry] == opponent_entry):
        return "win"
    elif (my_entry == opponent_entry):
        return "draw"
    else:
        return "loss"

for round in input_data_flat:
    if len(round_entries := round.split(" ")) == 2:
        opponent_entry, my_entry_presumed = round_entries
        my_entry = presumed_to_shape[my_entry_presumed]

        points += shape_points[my_entry]
        outcome = get_outcome_from_entries(opponent_entry, my_entry)

        points += outcome_points[outcome]

# %% Part 2: Forcing outcomes

input_to_outcome = {
    "X": "loss",
    "Y": "draw",
    "Z": "win",
}

def get_my_entry_for_outcome(outcome, opponent_entry):
    if outcome == "win":
        return win_lookup[opponent_entry]
    elif outcome == "loss":
        return loss_lookup[opponent_entry]
    else:
        return opponent_entry

points = 0
for round in input_data_flat:
    if len(round_entries := round.split(" ")) == 2:
        opponent_entry, outcome_input = round_entries
        outcome = input_to_outcome[outcome_input]

        my_entry = get_my_entry_for_outcome(outcome, opponent_entry)
        
        points += outcome_points[outcome]
        points += shape_points[my_entry]

# %%
