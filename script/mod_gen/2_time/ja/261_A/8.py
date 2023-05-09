def solve():
    l1,r1,l2,r2 = map(int,input().split())
    if l1 <= l2 <= r1 <= r2:
        print(r1-l2)
    elif l1 <= r2 <= r1 <= l2:
        print(r2-l1)
    elif l2 <= l1 <= r2 <= r1:
        print(r2-l1)
    elif l2 <= r1 <= r2 <= l1:
        print(r1-l2)
    else:
        print(0)

if __name__ == '__main__':
    solve()