# %%
from pathlib import Path
import numpy as np
# %%
# Loading input
with open(Path(".").parent / "input.txt", "r") as fh:
    input_data = fh.read()
input_data_flat = input_data.split("\n")

# %% DAY 1
input_data_grouped_sum = []

# Part 1: Grouping input and finding max
group_sum = 0
for line_value in input_data_flat:
    if line_value == "":
        input_data_grouped_sum.append(group_sum)
        group_sum = 0
        continue
    group_sum += int(line_value)

input_data_grouped_sum_sorted = np.sort(input_data_grouped_sum)
answer_1_1 = input_data_grouped_sum_sorted[-1]
print(answer_1_1)
# %% Part 2: Sum of 3 highest groups
answer_1_2 = input_data_grouped_sum_sorted[-3:].sum()
print(answer_1_2)
