def solve():
    a,b,c = map(int,input().split())
    print(100/(1-(a+b+c)/100))

if __name__ == '__main__':
    solve()