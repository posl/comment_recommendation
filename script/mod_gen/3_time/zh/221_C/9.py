def f(n):
    if n < 10:
        return n
    else:
        s = str(n)
        l = len(s)
        if l % 2 == 0:
            return int(s[0:l//2])*int(s[l//2:l])
        else:
            return max(int(s[0:l//2+1])*int(s[l//2+1:l]), int(s[0:l//2])*int(s[l//2:l]))

if __name__ == '__main__':
    f()