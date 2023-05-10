def swap(string, a, b):
    if a > b:
        a, b = b, a
    return string[:a-1] + string[b-1] + string[a:b-1] + string[a-1] + string[b:]
