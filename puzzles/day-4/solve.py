# %%
from pathlib import Path
import numpy as np
# %% Loading input
with open(Path(__file__).parent / "input.txt", "r") as fh:
    input_data = fh.read()
input_data_flat = input_data.split("\n")
input_data_flat = [i for i in input_data_flat if i]
# %% Part 1: Full overlap
overlapping_pairing_count = 0

for pairing in input_data_flat:
    ranges =  [r.split("-") for r in pairing.split(",")]
    ranges = np.array(ranges).astype(int)
    sections = [np.arange(*r + [0, 1]) for r in ranges]
    section_lengths = [len(s) for s in sections]
    intersections = np.intersect1d(*sections)  # Pun not intended
    if len(intersections) in section_lengths:
        overlapping_pairing_count += 1

# %% Part 2: Partial overlap
overlapping_pairing_count = 0

for pairing in input_data_flat:
    ranges =  [r.split("-") for r in pairing.split(",")]
    ranges = np.array(ranges).astype(int)
    sections = [np.arange(*r + [0, 1]) for r in ranges]
    section_lengths = [len(s) for s in sections]
    intersections = np.intersect1d(*sections)  # Pun not intended
    if len(intersections):
        overlapping_pairing_count += 1

# %%
