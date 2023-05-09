def main():
    S = input()
    K = int(input())
    N = len(S)
    ans = 0
    # 連続するXの数を数える
    cnt = 0
    for i in range(N):
        if S[i] == 'X':
            cnt += 1
        else:
            ans = max(ans, cnt)
            cnt = 0
    ans = max(ans, cnt)
    # 連続するXの数がK以下なら、全ての.をXに変える
    if ans <= K:
        ans = N
    # 連続するXの数がKより大きいなら、
    # 連続するXの数がK+1以上の部分を全てXに変える
    else:
        ans = 0
        cnt = 0
        for i in range(N):
            if S[i] == 'X':
                cnt += 1
            else:
                if cnt >= K + 1:
                    ans += cnt - K
                cnt = 0
        if cnt >= K + 1:
            ans += cnt - K
    print(ans)

if __name__ == '__main__':
    main()