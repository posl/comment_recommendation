def main():
    N, M, T = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    bat = N
    for i in range(M):
        bat -= A[i]
        if bat <= 0:
            print("No")
            return
        bat += B[i] - A[i]
        if bat > N:
            bat = N
    bat -= T - B[M-1]
    if bat <= 0:
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    main()