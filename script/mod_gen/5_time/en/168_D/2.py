def main():
    N, M = list(map(int, input().split()))
    A = []
    B = []
    for i in range(M):
        a, b = list(map(int, input().split()))
        A.append(a)
        B.append(b)
    print("Yes")
    for i in range(N-1):
        print(A[B.index(i+2)])

if __name__ == '__main__':
    main()