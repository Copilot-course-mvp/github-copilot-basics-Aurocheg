def group_by_domain(emails: list[str]) -> dict[str, int]:
    """Translate the JavaScript behavior above into Python."""
    counts: dict[str, int] = {}

    for email in emails:
        if "@" not in email:
            continue

        parts = email.split("@", 1)
        if len(parts) < 2:
            continue

        domain = parts[1].strip().lower()

        if not domain:
            continue

        counts[domain] = counts.get(domain, 0) + 1

    # sort keys alphabetically like JS Object.fromEntries + sort
    return dict(sorted(counts.items()))