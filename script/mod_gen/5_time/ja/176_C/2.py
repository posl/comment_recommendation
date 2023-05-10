def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = []
    for i in range(N):
        B.append(A[i] - i)
    B.sort()
    #print(B)
    min = B[0]
    for i in range(1, N):
        if B[i] - B[i-1] < min:
            min = B[i] - B[i-1]
    #print(min)
    ans = 0
    for i in range(N):
        ans += A[i] - (B[i] - min)
    print(ans)

if __name__ == '__main__':
    main()