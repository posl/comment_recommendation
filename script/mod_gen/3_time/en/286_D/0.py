def main():
    N, X = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    for i in range(2**N):
        sum = 0
        for j in range(N):
            if ((i>>j)&1):
                sum += A[j]*B[j]
        if sum == X:
            print("Yes")
            return
    print("No")

if __name__ == '__main__':
    main()