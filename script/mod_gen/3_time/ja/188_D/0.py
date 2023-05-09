def main():
    N, C = map(int, input().split())
    A = []
    B = []
    C = []
    for i in range(N):
        a, b, c = map(int, input().split())
        A.append(a)
        B.append(b)
        C.append(c)
    A.sort()
    B.sort()
    C.sort()
    #print(A)
    #print(B)
    #print(C)
    ans = 0
    for i in range(N):
        ans += A[i] * (N - i) + B[i] * (i + 1)
    print(ans)

if __name__ == '__main__':
    main()