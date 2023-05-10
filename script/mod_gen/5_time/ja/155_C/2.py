def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S.sort()
    S.append('')
    ans = []
    cnt = 1
    for i in range(N):
        if S[i] == S[i+1]:
            cnt += 1
        else:
            if cnt == 1:
                pass
            else:
                ans.append(S[i])
            cnt = 1
    for i in range(len(ans)):
        print(ans[i])

if __name__ == '__main__':
    main()