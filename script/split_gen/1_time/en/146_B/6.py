def shift(n, s):
    result = ""
    for c in s:
        if ord(c) + n > ord("Z"):
            result += chr(ord("A") + ord(c) + n - ord("Z") - 1)
        else:
            result += chr(ord(c) + n)
    return result
