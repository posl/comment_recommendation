def main():
    #入力
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    A = [0 for i in range(M)]
    B = [0 for i in range(M)]
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    #処理
    ans = 0
    for i in range(N):
        flag = True
        for j in range(M):
            if A[j] == i+1 and H[i] <= H[B[j]-1]:
                flag = False
                break
            elif B[j] == i+1 and H[i] <= H[A[j]-1]:
                flag = False
                break
        if flag:
            ans += 1
    #出力
    print(ans)

if __name__ == '__main__':
    main()