def solve():
    x,k,d = map(int,input().split())
    x = abs(x)
    if x >= k*d:
        return x - k*d
    else:
        k -= x//d
        x = x%d
        if k%2 == 0:
            return x
        else:
            return d - x

if __name__ == '__main__':
    solve()