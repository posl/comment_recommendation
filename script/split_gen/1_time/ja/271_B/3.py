def main():
    N, Q = map(int, input().split())
    A = []
    for i in range(N):
        a = list(map(int, input().split()))
        A.append(a)
    for i in range(Q):
        s, t = map(int, input().split())
        print(A[s-1][t])
