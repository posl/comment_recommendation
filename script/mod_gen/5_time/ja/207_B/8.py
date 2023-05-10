def solve():
    A,B,C,D = map(int,input().split())
    if A <= B:
        print(-1)
        return
    if D*C <= B:
        print(-1)
        return
    cnt = 0
    while A > C*D:
        A += B
        cnt += 1
    print(cnt)

if __name__ == '__main__':
    solve()