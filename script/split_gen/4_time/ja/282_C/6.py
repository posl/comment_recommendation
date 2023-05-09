def problems282_c():
    N = int(input())
    S = input()
    ans = ''
    cnt = 0
    for i in range(N):
        if S[i] == '"':
            cnt += 1
        elif S[i] == ',':
            if cnt % 2 == 0:
                ans += S[i]
            else:
                ans += '.'
        else:
            ans += S[i]
    print(ans)
