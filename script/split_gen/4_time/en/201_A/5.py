def is_arithmetic_sequence(a1, a2, a3):
    if a1 == a2 and a2 == a3:
        return True
    elif a1 == a2 or a2 == a3 or a1 == a3:
        return False
    elif a1 + a3 == 2 * a2:
        return True
    else:
        return False
a1, a2, a3 = map(int, input().split())
