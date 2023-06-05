def solve(x,a,d,n):
    if x < a:
        return a-x
    elif x == a:
        return 0
    else:
        if d == 0:
            return 0
        else:
            if x < a:
                return a-x
            else:
                if (x-a)%d == 0:
                    return (x-a)//d
                else:
                    return (x-a)//d + 1
