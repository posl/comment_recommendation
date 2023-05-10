def solve(a,b,c,d):
    ans = 0
    if b >= a:
        ans = 1
    else:
        if (a-b) % (b-c) == 0:
            ans = (a-b) // (b-c) + 1
        else:
            ans = (a-b) // (b-c) + 2
    return ans
