def main():
    from collections import deque
    import sys
    input = sys.stdin.readline
    Q = int(input())
    que = deque()
    ans = []
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            que.append(query[1])
            que.append(query[2])
        else:
            ans.append(sum(que.popleft() for _ in range(query[1])))
    print(*ans, sep='
')

if __name__ == '__main__':
    main()