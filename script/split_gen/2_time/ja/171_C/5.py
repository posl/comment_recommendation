def to26(n):
    if n == 0:
        return ""
    else:
        return to26((n-1)//26) + chr((n-1)%26+ord('a'))
print(to26(int(input())))
