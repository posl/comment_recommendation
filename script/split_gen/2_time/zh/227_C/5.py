def countABC(N):
    count = 0
    for a in range(1, N+1):
        for b in range(a, N+1):
            for c in range(b, N+1):
                if a*b*c <= N:
                    count += 1
    return count
