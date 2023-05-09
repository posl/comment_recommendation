def main():
    # input
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    # compute
    time = 0
    count = 0
    for i in range(N):
        if time + A[i] <= T:
            time += A[i]
            count += 1
        else:
            break
    # output
    print(count, T-time)
