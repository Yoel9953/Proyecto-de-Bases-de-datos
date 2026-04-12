def is_empty(*values: str) -> bool:
    return any(not value.strip() for value in values)