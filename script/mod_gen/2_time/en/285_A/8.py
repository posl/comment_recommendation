def solve():
    a,b = map(int,input().split())
    if a <= 8 and b >= 9:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    solve()