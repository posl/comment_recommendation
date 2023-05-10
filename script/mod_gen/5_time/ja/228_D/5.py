def main():
    import sys
    from collections import deque
    input = sys.stdin.readline
    N = 2**20
    Q = int(input())
    A = [-1]*N
    dq = deque()
    for _ in range(Q):
        t, x = map(int, input().split())
        if t == 1:
            h = x
            while A[h%N] != -1:
                h += 1
            A[h%N] = x
            dq.append(h%N)
        else:
            while A[x%N] == -1:
                x += 1
            print(A[x%N])
            A[x%N] = -1
            while dq and A[dq[0]] == -1:
                dq.popleft()
            if dq:
                A[dq[0]] = x
                dq.append(dq.popleft())

if __name__ == '__main__':
    main()