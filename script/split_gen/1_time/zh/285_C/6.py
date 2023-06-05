def problems285_c():
    s = input()
    sum = 0
    for i in range(1,len(s)):
        sum += 26 ** i
    sum += (ord(s[0]) - 64) * 26 ** (len(s) - 1)
    print(sum)
problems285_c()
