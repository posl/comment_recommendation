def solve():
    a,b = map(int,input().split())
    for n in range(1,100000):
        if int(n*0.08) == a and int(n*0.1) == b:
            print(n)
            return
    print(-1)

if __name__ == '__main__':
    solve()