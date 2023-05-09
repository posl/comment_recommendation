def solve(x,a,d,n):
    if d == 0:
        if x == a:
            return 0
        else:
            return -1
    else:
        if abs(x-a) % abs(d) == 0:
            return abs(x-a) // abs(d)
        else:
            return -1
x,a,d,n = map(int,input().split())
print(solve(x,a,d,n))

if __name__ == '__main__':
    solve()