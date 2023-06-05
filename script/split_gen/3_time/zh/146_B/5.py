def move(str,n):
    str1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    str2 = 'abcdefghijklmnopqrstuvwxyz'
    str3 = ''
    for s in str:
        if s in str1:
            str3 += str1[(str1.index(s)+n)%26]
        elif s in str2:
            str3 += str2[(str2.index(s)+n)%26]
        else:
            str3 += s
    return str3
