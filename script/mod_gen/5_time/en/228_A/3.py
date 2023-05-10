def problem():
    s, t, x = input().split()
    s = int(s)
    t = int(t)
    x = int(x)
    if s < t:
        if s < x and x < t:
            print('Yes')
        else:
            print('No')
    else:
        if s < x or x < t:
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    problem()