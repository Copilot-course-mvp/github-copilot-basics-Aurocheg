# Copilot Evidence — Step 05

## Documentation prompt

Generate concise Python docstrings for these functions with purpose, args, returns, and one example. Also write a USAGE.md guide with one quickstart example and one edge-case example.

## What you edited after Copilot output

I refined the wording to match the exact ValueError messages and added examples for both normal usage and edge cases.

## Accuracy check

I compared each docstring and USAGE.md example against the implementation: size/window <= 0 raises ValueError, chunk_list returns fixed-size chunks, and moving_average returns [] when the window is larger than the input.