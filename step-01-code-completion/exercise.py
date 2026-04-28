import re


def normalize_username(name: str) -> str:
    """Normalize a username.

    Rules:
    - Trim outer whitespace.
    - Convert to lowercase.
    - Replace spaces with underscores.
    - Remove any character that is not a-z, 0-9, or underscore.
    - Collapse repeated underscores into one underscore.
    - Strip leading/trailing underscores.
    """
    # Trim whitespace and convert to lowercase
    name = name.strip().lower()
    # Replace spaces with underscores
    name = name.replace(' ', '_')
    # Remove any character that is not a-z, 0-9, or underscore
    name = re.sub(r'[^a-z0-9_]', '', name)
    # Collapse repeated underscores into one
    name = re.sub(r'_+', '_', name)
    # Strip leading/trailing underscores
    name = name.strip('_')
    return name


def build_slug(title: str) -> str:
    """Convert a title into a URL-friendly slug.

    Rules:
    - Lowercase.
    - Keep letters and digits.
    - Replace any sequence of non-alphanumeric characters with a single '-'.
    - Strip leading/trailing '-'.
    """
    # Convert to lowercase
    title = title.lower()
    # Replace any sequence of non-alphanumeric characters with a single '-'
    title = re.sub(r'[^a-z0-9]+', '-', title)
    # Strip leading/trailing '-'
    title = title.strip('-')
    return title
