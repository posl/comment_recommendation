def get_max_value(n, values):
    if n == 2:
        return sum(values)/2
    else:
        values.sort()
        value = (values[0] + values[1])/2
        values.pop(0)
        values.pop(0)
        values.append(value)
        return get_max_value(n-1, values)

if __name__ == '__main__':
    get_max_value()