def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    print(sum([S[i][-3:] in T for i in range(N)]))

if __name__ == '__main__':
    main()