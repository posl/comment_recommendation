def main():
    N, x, y = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(N):
        for j in range(i+1, N):
            if A[i] > A[j]:
                A[i], A[j] = A[j], A[i]
    A.append(0)
    A.append(0)
    for i in range(N):
        for j in range(i+1, N+1):
            if A[i] > A[j]:
                A[i], A[j] = A[j], A[i]
    for i in range(N):
        if (A[i+1] - A[i]) % 2 == 1:
            print("No")
            exit()
    if (x-y) % 2 == 1:
        print("No")
        exit()
    print("Yes")

if __name__ == '__main__':
    main()