def main():
    S = input()
    K = int(input())
    N = len(S)
    ans = 0
    # 連続する X の数を数える
    cnt = 0
    for i in range(N):
        if S[i] == 'X':
            cnt += 1
        else:
            ans = max(ans, cnt)
            cnt = 0
    ans = max(ans, cnt)
    # X の数が K 以上の場合は、X を K 個連続させる
    if ans >= K:
        ans = K
    # X の数が K 未満の場合は、X を ans 個連続させる
    else:
        ans += (K - ans) // 2 * 2
    print(ans)

if __name__ == '__main__':
    main()