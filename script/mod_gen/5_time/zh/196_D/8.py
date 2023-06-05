def solve(h,w,a,b):
    if h%2==0 and w%2==0:
        return 3
    elif h%2==0 or w%2==0:
        return 2
    else:
        return 1

if __name__ == '__main__':
    solve()