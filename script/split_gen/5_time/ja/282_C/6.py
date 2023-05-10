def problems282_c():
    n = int(input())
    s = input()
    res = ""
    cnt = 0
    for i in range(n):
        if s[i] == '"':
            cnt += 1
            if cnt % 2 == 1:
                res += '"'
            else:
                res += '.'
        else:
            res += s[i]
    print(res)
