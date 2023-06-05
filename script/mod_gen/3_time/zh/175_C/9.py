def solve(x,k,d):
    if x < 0:
        x = -x
    if x >= k*d:
        return x-k*d
    else:
        y = x//d
        if (k-y)%2 == 0:
            return x-y*d
        else:
            return (y+1)*d-x

if __name__ == '__main__':
    solve()