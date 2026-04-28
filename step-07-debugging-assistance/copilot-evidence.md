# Copilot Evidence — Step 07

## Debug prompt

Why does this function fail for empty input, zero values, negative values, and average calculation? Explain the root causes.

## /fix prompt

/fix this function and preserve output schema. It should ignore negative values, include zero as valid, compute min, max, and average correctly, and return zeros when no valid values exist.

## Root cause summary

The original function excluded zero by using value > 0, initialized min and max to 0 instead of using valid data, and used integer division for the average. The fixed version filters only negative values, handles empty filtered data safely, and uses min, max, and true division.