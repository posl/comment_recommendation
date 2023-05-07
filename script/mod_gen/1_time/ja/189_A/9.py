def solve():
    a,b,c = map(str, input().split())
    if a==b and b==c:
        print("Won")
    else:
        print("Lost")

if __name__ == '__main__':
    solve()