def solve():
    A,B,C,D = map(int, input().split())
    if A <= B * D:
        print(-1)
    else:
        cnt = 0
        while A > B * D:
            A += B
            A -= C
            cnt += 1
        print(cnt)
    return 0
