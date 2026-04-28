# Usage Guide

## Quickstart

Use `chunk_list` to split a list into smaller fixed-size groups:

```python
from exercise import chunk_list, moving_average

chunks = chunk_list([1, 2, 3, 4, 5], 2)
print(chunks)
# [[1, 2], [3, 4], [5]]

averages = moving_average([10.0, 20.0, 30.0], 2)
print(averages)
# [15.0, 25.0]