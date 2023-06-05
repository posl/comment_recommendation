def check(s):
    for a in range(1, 1001):
        for b in range(1, 1001):
            if (4 * a * b + 3 * a + 3 * b) == s:
                return True
    return False
