def main():
    #入力
    N, M, X = map(int, input().split())
    C = []
    A = []
    for i in range(N):
        c, *a = map(int, input().split())
        C.append(c)
        A.append(a)
    
    #全探索
    ans = 10**9
    for i in range(2**N):
        #理解度の合計
        sum_a = [0]*M
        #合計金額
        sum_c = 0
        for j in range(N):
            if i >> j & 1:
                sum_c += C[j]
                for k in range(M):
                    sum_a[k] += A[j][k]
        #理解度がX以上か
        if all(a >= X for a in sum_a):
            ans = min(ans, sum_c)
    
    #出力
    if ans == 10**9:
        print(-1)
    else:
        print(ans)

if __name__ == '__main__':
    main()