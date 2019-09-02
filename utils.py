def validate_empty_values(**kwargs):
    for field in kwargs:
        value = kwargs.get(field)
        if isinstance(value, str):
            value = value.strip()
        if type(value) is not bool and not value:
            raise AttributeError(field + " is required")
