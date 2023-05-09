def reverse(n):
    n = str(n)
    n = n.replace("9", "x")
    n = n.replace("1", "9")
    n = n.replace("x", "1")
    return n
