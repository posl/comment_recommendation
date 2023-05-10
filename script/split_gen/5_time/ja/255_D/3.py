def main():
    N,Q = map(int,input().split())
    A = list(map(int,input().split()))
    X = []
    for _ in range(Q):
        X.append(int(input()))
    # print(N,Q,A,X)
    # N,Q,A,X = 10,5,[1000000000, 314159265, 271828182, 141421356, 161803398, 0, 777777777, 255255255, 536870912, 998244353],[555555555,321654987,1000000000,789456123,0]
    # print(N,Q,A,X)
    A.sort()
    # print(A)
    # print(X)
    for x in X:
        # print("x",x)
        # print("A",A)
        # print("A[-1]",A[-1])
        # print("A[0]",A[0])
        if x >= A[-1]:
            # print("x >= A[-1]",x,A[-1])
            print(x - A[-1] + N)
        elif x <= A[0]:
            # print("x <= A[0]",x,A[0])
            print(A[0] - x + N)
        else:
            # print("x in A",x,A)
            # print("A[0]",A[0])
            # print("A[-1]",A[-1])
            # print("A[0] + N - A[-1]",A[0] + N - A[-1])
            print(A[0] + N - A[-1])
