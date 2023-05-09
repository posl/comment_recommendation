def main():
    N, X = map(int, input().split())
    A, B = [], []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    for i in range(N):
        X = X - A[i]
        if X <= 0:
            print("No")
            return
        X = X + B[i]
        if X >= 10000:
            print("Yes")
            return
    print("No")
main()
