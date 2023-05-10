def solve():
    n = int(input())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab.sort(key=lambda x:x[0]+x[1], reverse=True)
    a_sum = sum([a for a, b in ab])
    b_sum = sum([b for a, b in ab])
    a_win = 0
    b_win = 0
    for a, b in ab:
        a_sum -= a
        b_sum -= b
        a_win += a
        b_win += b
        if a_win > b_sum:
            print(n - b_win)
            return
        if b_win > a_sum:
            print(n - a_win)
            return
    print(0)
    return
