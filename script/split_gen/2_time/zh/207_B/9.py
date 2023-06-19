def solution():
    A,B,C,D = map(int, input().split())
    if A < B:
        print(-1)
        return
    if A > B*D:
        print(-1)
        return
    if D == 1:
        print(0)
        return
    if B >= C*D:
        print(-1)
        return
    count = 1
    while True:
        if A <= B*D:
            print(count)
            return
        A += B
        A -= C
        count += 1
    print(-1)
