def main():
    import sys
    from collections import deque
    input = sys.stdin.readline
    N = 2 ** 20
    Q = int(input())
    A = [-1] * N
    q = deque()
    for _ in range(Q):
        t, x = map(int, input().split())
        if t == 1:
            h = x
            while A[h % N] != -1:
                h += 1
            A[h % N] = x
            q.append(h % N)
        else:
            if x <= q[0]:
                print(A[x])
            else:
                print(-1)

if __name__ == '__main__':
    main()