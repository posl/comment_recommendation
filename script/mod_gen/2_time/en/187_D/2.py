def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    C = []
    for i in range(N):
        C.append(A[i] + B[i])
    C.sort(reverse=True)
    takahashi = 0
    aoki = 0
    for i in range(N):
        takahashi += A[i]
    for i in range(N):
        aoki += B[i]
    if takahashi > aoki:
        print(0)
    else:
        for i in range(N):
            if takahashi > aoki:
                print(i)
                break
            takahashi += C[i]
            aoki -= C[i]

if __name__ == '__main__':
    main()