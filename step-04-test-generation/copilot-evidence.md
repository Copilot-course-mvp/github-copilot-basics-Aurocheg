# Copilot Evidence — Step 04

## Prompt used for test generation

Generate Python unittest cases for sanitize_tags including edge cases: empty input, duplicates with mixed case, punctuation, whitespace, empty tags after cleanup, and preserving order.

## Extra edge case Copilot missed

I added preserving first-seen order in addition to empty input, duplicate mixed-case tags, and punctuation because deduplication should not sort or reorder tags.

## Final test count

6 test methods, 6 assertions