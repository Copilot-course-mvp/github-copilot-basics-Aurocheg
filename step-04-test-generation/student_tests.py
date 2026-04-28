import unittest
import importlib.util
from pathlib import Path


def _load_exercise_module():
    module_path = Path(__file__).with_name("exercise.py")
    spec = importlib.util.spec_from_file_location("step04_exercise", module_path)
    module = importlib.util.module_from_spec(spec)
    assert spec is not None and spec.loader is not None
    spec.loader.exec_module(module)
    return module


exercise = _load_exercise_module()

class TestSanitizeTags(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(exercise.sanitize_tags([]), [])

    def test_duplicate_tags_with_mixed_case(self):
        self.assertEqual(
            exercise.sanitize_tags(["Python", "python", "PYTHON"]),
            ["python"],
        )

    def test_tags_containing_punctuation(self):
        self.assertEqual(
            exercise.sanitize_tags(["hello!", "#go", "full-stack", "data_science"]),
            ["hello", "go", "full-stack", "datascience"],
        )

    def test_trims_whitespace_and_lowercases(self):
        self.assertEqual(
            exercise.sanitize_tags(["  Go  ", " Rust "]),
            ["go", "rust"],
        )

    def test_removes_empty_tags_after_cleanup(self):
        self.assertEqual(
            exercise.sanitize_tags(["   ", "!!!", "@@@", "Go"]),
            ["go"],
        )

    def test_preserves_first_seen_order(self):
        self.assertEqual(
            exercise.sanitize_tags(["Go", "Python", "go", "Rust", "python"]),
            ["go", "python", "rust"],
        )

if __name__ == "__main__":
    unittest.main()