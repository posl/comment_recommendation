def get_max_value(values):
    if len(values) == 1:
        return values[0]
    max_value = 0
    for i in range(len(values)):
        for j in range(i+1, len(values)):
            new_value = (values[i] + values[j]) / 2
            new_values = values[:i] + values[i+1:j] + values[j+1:]
            new_values.append(new_value)
            value = get_max_value(new_values)
            if value > max_value:
                max_value = value
    return max_value
