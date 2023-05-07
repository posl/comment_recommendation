def solve():
    A,B,C = map(int,input().split())
    print((A*(A+1)/2)/(A+B+C))

if __name__ == '__main__':
    solve()