def get_char(n):
    if n <= 26:
        return chr(96+n)
    else:
        return get_char((n-1)//26) + chr(96+(n-1)%26+1)
n = int(input())
print(get_char(n))
