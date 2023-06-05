def get_str(n):
    if n <= 26:
        return chr(n+96)
    else:
        return get_str((n-1)//26) + chr((n-1)%26+97)
