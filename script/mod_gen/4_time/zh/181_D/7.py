def check(s):
    s = list(s)
    for i in range(len(s)):
        if s[i] == '0':
            return False
        s[i] = int(s[i])
    for i in range(1,10):
        if s.count(i) > 4:
            return False
    for i in range(1,10):
        for j in range(1,10):
            for k in range(1,10):
                for l in range(1,10):
                    s1 = s.copy()
                    if i in s1:
                        s1.remove(i)
                    if j in s1:
                        s1.remove(j)
                    if k in s1:
                        s1.remove(k)
                    if l in s1:
                        s1.remove(l)
                    if len(s1) == 0:
                        if (i*1000+j*100+k*10+l)%8 == 0:
                            return True
    return False
s = input()

if __name__ == '__main__':
    check()