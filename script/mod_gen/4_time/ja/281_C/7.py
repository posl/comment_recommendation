def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    A = A * 2
    s = 0
    for i in range(N):
        s += A[i]
    t = T % s
    if t == 0:
        t = s
    s = 0
    for i in range(N * 2):
        s += A[i]
        if s >= t:
            print(i + 1, t)
            break

if __name__ == '__main__':
    main()