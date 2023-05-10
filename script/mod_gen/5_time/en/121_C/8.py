def main():
    import sys
    from collections import deque
    input = sys.stdin.readline
    N, M = map(int, input().split())
    A = deque()
    B = deque()
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    ans = 0
    while M > 0:
        a = A.popleft()
        b = B.popleft()
        if M > b:
            ans += a * b
            M -= b
        else:
            ans += a * M
            M = 0
    print(ans)

if __name__ == '__main__':
    main()