def solve():
    x,y = map(int,input().split())
    for i in range(x+1):
        if i*2 + (x-i)*4 == y:
            print("Yes")
            return
    print("No")

if __name__ == '__main__':
    solve()