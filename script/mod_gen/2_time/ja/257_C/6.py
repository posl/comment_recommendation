def main():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    #print(N, S, W)
    # 体重の昇順に並び替える
    W.sort()
    # Xの候補を列挙する
    X = []
    for i in range(N-1):
        if W[i] != W[i+1]:
            X.append((W[i] + W[i+1]) / 2)
    #print(X)
    # Xの候補の中で最大値を求める
    ans = 0
    for x in X:
        cnt = 0
        for i in range(N):
            if W[i] < x and S[i] == '0':
                cnt += 1
            elif W[i] >= x and S[i] == '1':
                cnt += 1
        ans = max(ans, cnt)
    print(ans)

if __name__ == '__main__':
    main()