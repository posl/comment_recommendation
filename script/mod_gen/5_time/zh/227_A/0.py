def solve():
    n,k,a = map(int, input().split())
    if (k-n)%(n-1) == 0:
        print(a)
    else:
        print((k-n)%(n-1)+a)

if __name__ == '__main__':
    solve()