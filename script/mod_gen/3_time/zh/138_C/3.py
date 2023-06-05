def max_value(v):
    if len(v) == 2:
        return (v[0] + v[1]) / 2
    else:
        v.sort(reverse=True)
        v[1] = (v[0] + v[1]) / 2
        v.pop(0)
        return max_value(v)

if __name__ == '__main__':
    max_value()