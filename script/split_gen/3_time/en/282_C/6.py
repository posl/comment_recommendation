def solve():
    N = int(input())
    S = input()
    if N % 2:
        print('error')
        return
    ans = ''
    cnt = 0
    for i in range(N):
        if S[i] == '"':
            cnt += 1
        elif cnt % 2:
            ans += S[i].replace(',', '.')
        else:
            ans += S[i]
    print(ans)
