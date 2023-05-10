def problems282_c():
    n = int(input())
    s = input()
    cnt = 0
    ans = ''
    for i in range(n):
        if s[i] == '"':
            cnt += 1
        elif s[i] == ',':
            if cnt % 2 == 0:
                ans += ','
            else:
                ans += '.'
        else:
            ans += s[i]
    print(ans)
