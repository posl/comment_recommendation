def main():
    # 入力
    N = int(input())
    a = list(map(int, input().split()))
    # 処理
    ans = []
    for i in range(N):
        if a[i] == 1:
            ans.append(i+1)
            for j in range(2, N//(i+1)+1):
                a[j*(i+1)-1] = 1 - a[j*(i+1)-1]
    # 出力
    if sum(a) == 0:
        print(len(ans))
        print(*ans)
    else:
        print(-1)

if __name__ == '__main__':
    main()