def main():
    N = int(input())
    V = list(map(int, input().split()))
    A, B = [], []
    for i in range(N):
        if i % 2 == 0:
            A.append(V[i])
        else:
            B.append(V[i])
    A.sort()
    B.sort()
    A.append(0)
    B.append(0)
    if A[0] == A[-2]:
        a = A[-1]
    else:
        a = A[0]
    if B[0] == B[-2]:
        b = B[-1]
    else:
        b = B[0]
    if a == b:
        if A.count(A[0]) > B.count(B[0]):
            print(N - A.count(A[0]))
        else:
            print(N - B.count(B[0]))
    else:
        print(N - A.count(a) - B.count(b))

if __name__ == '__main__':
    main()