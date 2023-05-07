def solve():
    a,b,c,d = map(int, input().split())
    return max(a*c,a*d,b*c,b*d)
print(solve())

if __name__ == '__main__':
    solve()