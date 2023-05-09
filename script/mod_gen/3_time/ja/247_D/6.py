def main():
    from sys import stdin
    input = stdin.readline
    from collections import deque
    Q = int(input())
    d = deque()
    ans = 0
    for i in range(Q):
        query = list(map(int,input().split()))
        if query[0] == 1:
            for j in range(query[2]):
                d.append(query[1])
        else:
            for j in range(query[1]):
                ans += d.popleft()
            print(ans)
            ans = 0

if __name__ == '__main__':
    main()