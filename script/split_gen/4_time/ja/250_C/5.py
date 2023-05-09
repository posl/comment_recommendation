def main():
    N, Q = map(int, input().split())
    A = list(range(1,N+1))
    for i in range(Q):
        x = int(input())
        a = A.index(x)
        A[a], A[a-1] = A[a-1], A[a]
    print(*A)
