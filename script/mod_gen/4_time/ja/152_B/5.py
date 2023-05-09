def solve():
    a,b = map(int,input().split())
    print(str(a)*b if a < b else str(b)*a)

if __name__ == '__main__':
    solve()