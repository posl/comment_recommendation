def main():
    from sys import stdin
    from collections import deque
    input = stdin.readline
    Q = int(input())
    queue = deque()
    ans = 0
    for i in range(Q):
        query = list(map(int,input().split()))
        if query[0] == 1:
            queue.append(query[1])
            ans += query[1]*query[2]
        else:
            ans -= queue.popleft()*query[1]
            print(ans)
main()
