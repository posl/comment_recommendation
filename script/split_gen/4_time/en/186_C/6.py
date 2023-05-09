def check(n):
    if '7' in str(n):
        return False
    if '7' in oct(n):
        return False
    return True
