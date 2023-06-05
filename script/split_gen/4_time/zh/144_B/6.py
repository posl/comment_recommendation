def check(n):
    for i in range(1,10):
        for j in range(1,10):
            if i * j == n:
                return True
    return False
