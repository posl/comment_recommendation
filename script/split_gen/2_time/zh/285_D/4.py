def problem285_c():
    s = input()
    length = len(s)
    sum = 0
    for i in range(length):
        sum += (ord(s[i])-ord('A')+1)*(26**(length-i-1))
    print(sum)
