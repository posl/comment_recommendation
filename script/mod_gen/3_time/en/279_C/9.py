def check_pattern(S, T):
    S = sorted(S)
    T = sorted(T)
    if S == T:
        return True
    else:
        return False

if __name__ == '__main__':
    check_pattern()