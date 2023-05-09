def count(S, T):
    cnt = 0
    for a in range(S + 1):
        for b in range(S + 1):
            for c in range(S + 1):
                if a + b + c <= S and a * b * c <= T:
                    cnt += 1
    return cnt
