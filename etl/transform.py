def transform(data):
    """
    Transform step:
    - Add a new field 'age_plus_1' for each record.
    """
    transformed = []
    for row in data:
        new_row = row.copy()
        new_row["age_plus_1"] = row["age"] + 1
        transformed.append(new_row)
    return transformed
