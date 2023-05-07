def solve():
    a,b,c = map(str, input().split())
    if a==b and b==c:
        print("Won")
    else:
        print("Lost")
