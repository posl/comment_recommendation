def main():
    N, M = map(int, input().split())
    S = [input() for i in range(N)]
    T = [input() for i in range(M)]
    for a in S:
        for b in S:
            for c in S:
                for d in S:
                    s = a + "_" + b + "_" + c + "_" + d
                    if s.count("_") == N and len(s) >= 3 and len(s) <= 16 and s not in T:
                        print(s.replace("_", ""))
                        return
    print(-1)
main()

if __name__ == '__main__':
    main()