def judge(a,s):
    if s < a:
        return False
    if s == a:
        return True
    if s > 2 * a:
        return False
    if s == 2 * a:
        return True
    if a % 2 == 0:
        return True
    else:
        return False
