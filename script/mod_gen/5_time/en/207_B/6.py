def solve():
    A,B,C,D = map(int, input().split())
    if A <= B*D:
        print(-1)
        return
    if B >= C*D:
        print(-1)
        return
    if B >= A:
        print(1)
        return
    print((A-B-1)//(C*D-B)+1)

if __name__ == '__main__':
    solve()