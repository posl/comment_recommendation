def main():
    import sys
    from collections import deque
    input = sys.stdin.readline
    n = int(input())
    q = deque()
    ans = 0
    for i in range(n):
        query = input().split()
        if query[0] == '1':
            q.append((int(query[1]), int(query[2])))
            ans += int(query[2])
        else:
            x = int(query[1])
            while x > 0:
                if x >= q[0][1]:
                    x -= q[0][1]
                    ans -= q[0][1] * q[0][0]
                    q.popleft()
                else:
                    ans -= x * q[0][0]
                    q[0] = (q[0][0], q[0][1] - x)
                    x = 0
            print(ans)
