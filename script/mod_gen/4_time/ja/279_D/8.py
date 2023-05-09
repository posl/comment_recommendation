def solve():
    a,b = map(int,input().split())
    if a >= b:
        print(a)
        return
    else:
        print(a + b/2)

if __name__ == '__main__':
    solve()