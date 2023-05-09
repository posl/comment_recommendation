def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    C = [0] * N
    for i in range(N):
        B[i] = A[i] % 200
    for i in range(N):
        C[i] = A[i] % 200
    B.sort()
    C.sort()
    for i in range(N):
        if B[i] == C[i]:
            print("No")
            return
    print("Yes")
    for i in range(N):
        print(B[i], end=" ")
    print()
    for i in range(N):
        print(C[i], end=" ")
    print()

if __name__ == '__main__':
    main()