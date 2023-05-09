def solve(x,k,d):
    if x < 0:
        x = -1 * x
    if x >= k*d:
        return x - k*d
    else:
        n = x//d
        x -= n*d
        k -= n
        if k%2 == 0:
            return x
        else:
            return d-x
x,k,d = map(int,input().split())
print(solve(x,k,d))

if __name__ == '__main__':
    solve()