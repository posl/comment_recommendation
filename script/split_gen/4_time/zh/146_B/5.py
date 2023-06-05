def move_str(s,n):
    a = []
    for i in s:
        if ord(i)+n>90:
            a.append(chr(ord(i)+n-26))
        else:
            a.append(chr(ord(i)+n))
    return ''.join(a)
