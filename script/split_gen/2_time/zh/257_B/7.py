def get_char(n,x):
    if n == 1:
        return chr(ord('A')+x-1)
    else:
        return get_char(n-1,x-(n-1)*26)
