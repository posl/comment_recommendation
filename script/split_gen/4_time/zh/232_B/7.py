def move(s, k):
    if k == 0:
        return s
    else:
        tmp = ''
        for i in range(len(s)):
            if ord(s[i])+k <= ord('z'):
                tmp += chr(ord(s[i])+k)
            else:
                tmp += chr(ord('a') + (ord(s[i])+k)%ord('z')-1)
        return tmp
