def main():
    N = int(input())
    S = [input() for _ in range(N)]
    S.sort()
    cnt = 1
    max_cnt = 0
    ans = []
    for i in range(N-1):
        if S[i] == S[i+1]:
            cnt+=1
        else:
            if cnt > max_cnt:
                ans = [S[i]]
                max_cnt = cnt
            elif cnt == max_cnt:
                ans.append(S[i])
            cnt = 1
    if cnt > max_cnt:
        ans = [S[-1]]
    elif cnt == max_cnt:
        ans.append(S[-1])
    for i in range(len(ans)):
        print(ans[i])

if __name__ == '__main__':
    main()