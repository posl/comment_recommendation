def get_name(n):
    name = ""
    while n > 0:
        n -= 1
        name = chr(n%26+97) + name
        n //= 26
    return name
