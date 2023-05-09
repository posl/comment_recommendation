def solve():
    W = int(input())
    if W <= 2:
        print("NO")
    elif W % 2 == 0:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    solve()