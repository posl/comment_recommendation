def solve():
    A, B, C, D = map(int, input().split())
    if B >= C * D:
        print(-1)
        return
    else:
        count = 0
        while A > 0:
            A -= B
            count += 1
            if A <= 0:
                break
            else:
                A += C
        print(count)
