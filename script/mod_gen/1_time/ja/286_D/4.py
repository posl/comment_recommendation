def main():
    N, X = map(int, input().split())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    #print(A)
    #print(B)
    ans = "No"
    for i in range(N):
        for j in range(B[i]+1):
            if A[i]*j==X:
                ans = "Yes"
                break
    print(ans)

if __name__ == '__main__':
    main()