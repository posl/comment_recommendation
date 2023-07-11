def solve():
    a,b,c = map(int, input().split())
    if a==b and b!=c:
        print("Yes")
    elif a==c and c!=b:
        print("Yes")
    elif b==c and c!=a:
        print("Ye

if __name__ == '__main__':
    solve()