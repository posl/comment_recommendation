def main():
    # Get input
    N, Q = map(int, input().split())
    L = []
    A = []
    for i in range(N):
        l, *a = map(int, input().split())
        L.append(l)
        A.append(a)
    ST = []
    for i in range(Q):
        s, t = map(int, input().split())
        ST.append((s, t))
    # Solve
    for s, t in ST:
        print(A[s-1][t-1])
    return
