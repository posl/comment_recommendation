def main():
    N, Q = list(map(int, input().split()))
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))
    for i in range(Q):
        s, t = list(map(int, input().split()))
        print(A[s-1][t])
