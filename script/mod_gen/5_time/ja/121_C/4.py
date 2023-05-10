def main():
    import sys
    readline = sys.stdin.readline
    N,M = map(int,readline().split())
    AB = [list(map(int,readline().split())) for _ in range(N)]
    AB.sort(key = lambda x:x[0])
    res = 0
    for a,b in AB:
        if M <= b:
            res += a * M
            break
        else:
            res += a * b
            M -= b
    print(res)

if __name__ == '__main__':
    main()