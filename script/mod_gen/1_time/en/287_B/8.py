def main():
    #input
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    #compute
    ans = 0
    for s in S:
        for t in T:
            if s[-3:] == t:
                ans += 1
                break
    #output
    print(ans)

if __name__ == '__main__':
    main()