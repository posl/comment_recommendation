def main():
    #入力
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    #解答
    ans = 0
    for i in range(N):
        ans += B[A[i]-1]
        if i != N-1:
            if A[i] == A[i+1]-1:
                ans += C[A[i]-1]
    #出力
    print(ans)

if __name__ == '__main__':
    main()