def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S.sort()
    ans = []
    cnt = 1
    for i in range(1,N):
        if S[i] == S[i-1]:
            cnt += 1
        else:
            if cnt > 1:
                ans.append(S[i-1])
            cnt = 1
    if cnt > 1:
        ans.append(S[N-1])
    for i in ans:
        print(i)

if __name__ == '__main__':
    main()