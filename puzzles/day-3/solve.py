# %%
from pathlib import Path
import numpy as np
from functools import reduce
import string
# %% Loading input
with open(Path(__file__).parent / "input.txt", "r") as fh:
    input_data = fh.read()
input_data_flat = input_data.split("\n")
# Filter out newline
input_data_flat =  np.array(
    [np.array(list(i)) for i in input_data_flat if len(i)],
    dtype=object
)
# %% Part 1
priority_lookup = dict(zip(
    list(string.ascii_lowercase[:26]
        + string.ascii_uppercase[:26]),
    list(np.arange(26 * 2) + 1)
))
# %%
priority_sum = 0
for items in input_data_flat:
    print(items)
    comp_a_items, comp_b_items = items.reshape(2, -1)

    duplicate_item = np.intersect1d(comp_a_items, comp_b_items)
    assert len(duplicate_item) == 1
    duplicate_item = duplicate_item[0]

    priority_sum += priority_lookup[duplicate_item]

# %% Part 2
priority_sum = 0
for group in np.array(input_data_flat).reshape(-1, 3):
    badge = reduce(np.intersect1d, group)
    assert len(badge) == 1
    badge = badge[0]
    priority_sum += priority_lookup[badge]

# %%
