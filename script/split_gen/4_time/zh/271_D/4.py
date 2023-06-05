def solve():
    N, S = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(N)]
    # print(N, S, AB)
    if any(a + b == S for a, b in AB):
        print('Yes')
        for a, b in AB:
            if a + b == S:
                print('H', end='')
            else:
                print('T', end='')
        print()
        return
    else:
        print('No')
        return
