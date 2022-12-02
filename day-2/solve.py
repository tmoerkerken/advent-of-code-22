# %%
from pathlib import Path
import numpy as np
# %%
# Loading input
with open(Path(__file__).parent / "input.txt", "r") as fh:
    input_data = fh.read()
input_data_flat = input_data.split("\n")
# Rule scoring maps
shape_points = {
    "X": 1,  # Rock
    "Y": 2,  # Paper
    "Z": 3,  # Scissors
}

outcome_points = {
    "loss": 0,
    "draw": 3,
    "win": 6,
}

# %% Part 1: Score according to guide

