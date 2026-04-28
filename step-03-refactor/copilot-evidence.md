# Copilot Evidence — Step 03

## Refactor prompt

Refactor this file to remove duplicated discount logic. Extract a helper named apply_discount and keep all public function signatures unchanged.

## Why behavior is preserved

The subtotal calculation remains inside each public function, and the extracted helper contains the same discount calculation, zero-or-negative discount handling, negative total clamp, and rounding logic as before.

## Before vs after summary

Before, checkout_total and invoice_total duplicated the same discount calculation. After, both functions calculate their subtotal and call apply_discount to share the discount behavior.