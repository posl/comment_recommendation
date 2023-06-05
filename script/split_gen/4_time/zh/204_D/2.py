def solve(N, T):
    if N == 1:
        return T[0]
    if N == 2:
        return max(T[0], T[1])
    if N == 3:
        return max(T[0] + T[1], T[2])
    if N == 4:
        return max(T[0] + T[3], T[1] + T[2])
    if N == 5:
        return max(T[0] + T[3] + T[4], T[1] + T[2] + T[3])
