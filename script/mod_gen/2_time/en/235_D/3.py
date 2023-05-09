def solve(a, N):
    if a == 1:
        if N == 1:
            return 0
        else:
            return -1
    if a == N:
        return 1
    if a > N:
        return -1
    if N % a != 0:
        return -1
    # Now we have 1 < a < N and N % a == 0
    # We need to find x such that x = N / a
    # We can do this by dividing N by a until we get 1
    # and count the number of divisions
    # but we can do it faster by counting the number of
    # times we can divide a by a until we get N
    # and then divide N by a that many times
    # For example, if a = 2 and N = 16, we can divide a by a 4 times
    # to get 16
    # If a = 3 and N = 27, we can divide a by a 3 times
    # to get 27
    # If a = 4 and N = 64, we can divide a by a 3 times
    # to get 64
    # If a = 5 and N = 125, we can divide a by a 3 times
    # to get 125
    # If a = 6 and N = 216, we can divide a by a 3 times
    # to get 216
    # If a = 7 and N = 343, we can divide a by a 3 times
    # to get 343
    # If a = 8 and N = 512, we can divide a by a 3 times
    # to get 512
    # If a = 9 and N = 729, we can divide a by a 3 times
    # to get 729
    # If a = 10 and N = 1000, we can divide a by a 3 times
    # to get 1000
    # If a = 11 and N = 1331, we can divide a by a 3 times
    # to get 1331
    # If a = 12 and N = 1728, we can divide a by a 3 times

if __name__ == '__main__':
    solve()