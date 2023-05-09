def solve():
    a,s=map(int,input().split())
    if a>s:
        print("No")
        return
    if (s-a)%2==0:
        print("Yes")
    else:
        print("No")
    return

if __name__ == '__main__':
    solve()