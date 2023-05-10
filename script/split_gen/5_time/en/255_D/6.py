def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for i in range(Q)]
    A.sort()
    A.append(0)
    A.append(10**9+1)
    A.sort()
    A = [A[i+1]-A[i] for i in range(N+1)]
    A.sort()
    A = [A[i+1]-A[i] for i in range(N)]
    #print(A)
    #print(X)
    s = sum(A)
    for x in X:
        print(s-x)
