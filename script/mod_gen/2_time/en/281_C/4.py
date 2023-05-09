def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    t = 0
    for i in range(N):
        if t <= T and T <= t + A[i]:
            print(i + 1, T - t)
            return
        else:
            t += A[i]
    T = T % t
    for i in range(N):
        if t <= T and T <= t + A[i]:
            print(i + 1, T - t)
            return
        else:
            t += A[i]

if __name__ == '__main__':
    main()