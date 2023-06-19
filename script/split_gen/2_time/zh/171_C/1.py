def get_str(n):
    if n == 0:
        return ''
    elif n <= 26:
        return chr(96+n)
    else:
        return get_str((n-1)//26) + get_str((n-1)%26+1)
    
n = int(input())
print(get_str(n))
