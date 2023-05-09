def main():
    N, M = map(int, input().split())
    sc = [list(map(int, input().split())) for _ in range(M)]
    if N == 1:
        for s, c in sc:
            if s == 1 and c == 0:
                print(-1)
                return
        print(0)
        return
    for i in range(1000):
        if len(str(i)) == N:
            for s, c in sc:
                if str(i)[s-1] != str(c):
                    break
            else:
                print(i)
                return
    print(-1)

if __name__ == '__main__':
    main()