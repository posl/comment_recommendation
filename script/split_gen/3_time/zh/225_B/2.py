def is_star(n, a, b):
    if n-1 != len(a) or n-1 != len(b):
        return False
    else:
        if len(set(a)) == len(set(b)) == len(set(a+b)) == n-1:
            return True
        else:
            return False
