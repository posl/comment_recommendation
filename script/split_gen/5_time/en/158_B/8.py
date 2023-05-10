def calc_blue_balls(N, A, B):
    #print("N: {}, A: {}, B: {}".format(N, A, B))
    if A == 0:
        return 0
    elif A + B == 1:
        return 1
    elif N <= A:
        return 1
    else:
        return A + (N - A) % (A + B)
