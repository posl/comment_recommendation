def main():
    n = int(input())
    A = list(map(int, input().split()))
    # Aの値をインデックスとするリストを作成
    B = [[] for _ in range(n)]
    for i in range(n):
        B[A[i]-1].append(i)
    # Bの要素数が1の場合は0を出力
    for i in range(n):
        if len(B[i]) == 1:
            print(0)
            exit()
    # Bの要素数が2の場合は1を出力
    for i in range(n):
        if len(B[i]) == 2:
            print(1)
            exit()
    # Bの要素数が3以上の場合は以下の処理を行う
    ans = []
    for i in range(n):
        if len(B[i]) >= 3:
            ans.append(len(B[i]) * (len(B[i])-1) // 2)
    # ansの要素数が1の場合は0を出力
    if len(ans) == 1:
        print(0)
        exit()
    # ansの要素数が2の場合は1を出力
    if len(ans) == 2:
        print(1)
        exit()
    # ansの要素数が3以上の場合は以下の処理を行う
    ans.sort()
    print(ans[0] + ans[1])

if __name__ == '__main__':
    main()