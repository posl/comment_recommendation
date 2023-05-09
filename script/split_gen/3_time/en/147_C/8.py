def is_honest(n, honest, testimony):
    for i in range(n):
        if honest[i]:
            for x, y in testimony[i]:
                if honest[x-1] != bool(y):
                    return False
    return True
