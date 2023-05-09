def get_num_of_blue_balls(N, A, B):
    if A == 0:
        return 0
    if B == 0:
        return N
    if A + B > N:
        return (N // (A + B)) * A + min(A, N % (A + B))
    return (N // (A + B)) * A + A
