def solve():
    a,b,c,d = map(int, input().split())
    if a <= b*d:
        print(-1)
    else:
        print((a+b*d-1)//(b*c-d))

if __name__ == '__main__':
    solve()