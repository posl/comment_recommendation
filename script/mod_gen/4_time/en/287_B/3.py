def main():
    N, M = map(int, input().split())
    S = [input() for i in range(N)]
    T = [input() for i in range(M)]
    count = 0
    for s in S:
        for t in T:
            if s.endswith(t):
                count += 1
                break
    print(count)

if __name__ == '__main__':
    main()