def main():
    N, Q = map(int, input().split())
    seq = []
    for i in range(N):
        seq.append(list(map(int, input().split())))
    for i in range(Q):
        s, t = map(int, input().split())
        print(seq[s-1][t-1])

if __name__ == '__main__':
    main()