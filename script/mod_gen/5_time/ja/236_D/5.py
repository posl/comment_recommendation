def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))
    #print(A)
    # 2人組の組み合わせをbit全探索
    ans = 0
    for i in range(1, 2**N):
        # iを2進数に変換
        bit = bin(i)[2:]
        #print(bit)
        # 2人組の相性の合計値を計算
        tmp = 0
        for j in range(N):
            for k in range(j+1, N):
                #print(j, k)
                if bit[j] == "1" and bit[k] == "1":
                    tmp += A[j][k]
        #print(tmp)
        ans = max(ans, tmp)
    print(ans)

if __name__ == '__main__':
    main()