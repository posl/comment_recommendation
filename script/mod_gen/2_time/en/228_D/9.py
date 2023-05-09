def main():
    import sys
    input = sys.stdin.readline
    from collections import deque
    N = 2**20
    A = [-1]*N
    Q = int(input())
    q = deque()
    for i in range(Q):
        t,x = map(int,input().split())
        if t == 1:
            q.append(x)
        else:
            if A[x%N] == -1:
                A[x%N] = q.popleft()
            print(A[x%N])
    return

if __name__ == '__main__':
    main()