def main():
    N, Q = map(int, input().split())
    L = [list(map(int, input().split())) for _ in range(N)]
    seq = [sum(L[i]) for i in range(N)]
    for i in range(1, N):
        seq[i] += seq[i - 1]
    for _ in range(Q):
        s, t = map(int, input().split())
        if s == 1:
            print(L[0][t - 1])
        else:
            print(L[s - 1][t - 1 - seq[s - 2]])

if __name__ == '__main__':
    main()