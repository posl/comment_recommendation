def count_bounce_times(N, X, L):
    D = [0] * (N + 1)
    D[0] = 0
    for i in range(1, N + 1):
        D[i] = D[i - 1] + L[i - 1]
    count = 0
    for d in D:
        if d <= X:
            count += 1
    return count

if __name__ == '__main__':
    count_bounce_times()