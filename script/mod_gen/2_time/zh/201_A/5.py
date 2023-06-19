def is_arithmetic_sequence(a1, a2, a3):
    if a1 == a2 == a3:
        return True
    elif a1 == a2 or a2 == a3:
        return False
    else:
        return (a3 - a2) == (a2 - a1)

if __name__ == '__main__':
    is_arithmetic_sequence()