def solve(a, s):
    #print("a=%d, s=%d" % (a, s))
    if a > s:
        return False
    if a == s:
        return True
    if a == 0:
        return False
    
    x = a
    y = s - a
    if x & y == a:
        return True
    else:
        return False

if __name__ == '__main__':
    solve()