def solve():
    a,b,c = map(int,input().split())
    print(max(a+b,b+c,c+a))
    return 0

if __name__ == '__main__':
    solve()