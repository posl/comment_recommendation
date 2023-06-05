def solve(x,y,a,b):
    if a == 1:
        if (y-x) % b == 0:
            return (y-x)//b
        else:
            return (y-x)//b + 1
    else:
        if b == 1:
            return y-x-1
        else:
            if a > b:
                if (y-x) % b == 0:
                    return (y-x)//b
                else:
                    return (y-x)//b + 1
            else:
                count = 0
                while x < y:
                    if (y-x) % b == 0:
                        return count + (y-x)//b
                    else:
                        count += 1
                        x *= a
                return count
x,y,a,b = map(int,input().split())
print(solve(x,y,a,b))
