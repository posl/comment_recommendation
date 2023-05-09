def main():
    N, K = map(int, input().split())
    S = input()
    if N == 1:
        print(1)
        return
    if N == K:
        print(N)
        return
    if N == K + 1:
        if S[0] == '0' or S[-1] == '0':
            print(N)
        else:
            print(N - 1)
        return
    if S[0] == '0':
        S = '0' + S
    if S[-1] == '0':
        S = S + '0'
    S = S + S
    N = len(S)
    #print(S)
    #print(N)
    start = []
    end = []
    for i in range(N):
        if S[i] == '0':
            start.append(i)
        else:
            end.append(i)
    #print(start)
    #print(end)
    ans = 0
    for i in range(len(start)):
        if i == 0:
            ans = max(ans, end[i])
        else:
            ans = max(ans, end[i] - start[i - 1])
    print(ans)

if __name__ == '__main__':
    main()