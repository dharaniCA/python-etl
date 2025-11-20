from etl.transform import transform


def test_transform_adds_age_plus_1():
    input_data = [
        {"name": "Alice", "age": 24},
        {"name": "Bob", "age": 30},
    ]

    result = transform(input_data)

    assert len(result) == 2
    assert result[0]["age_plus_1"] == 25
    assert result[1]["age_plus_1"] == 31
