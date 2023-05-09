def main():
    import sys
    read = sys.stdin.buffer.read
    readline = sys.stdin.buffer.readline
    readlines = sys.stdin.buffer.readlines
    N, D = map(int, readline().split())
    X, Y = map(int, read().split())
    ans = 0
    for i in range(N):
        if X**2 + Y**2 <= D**2:
            ans += 1
        X, Y = map(int, readline().split())
    print(ans)

if __name__ == '__main__':
    main()