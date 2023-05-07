def solve():
    A, B, C, D = map(int, input().split())
    if B >= C*D:
        print(-1)
    else:
        count = 0
        while A > 0:
            count += 1
            A -= B
            if A <= 0:
                break
            A += C
        print(count)
