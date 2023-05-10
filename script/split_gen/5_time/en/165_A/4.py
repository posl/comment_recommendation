def golf(k, a, b):
    for i in range(a, b+1):
        if i % k == 0:
            return "OK"
    return "NG"
