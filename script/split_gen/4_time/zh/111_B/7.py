def get_abc(n):
    if n%111 == 0:
        return n
    else:
        return (n//111 + 1)*111
