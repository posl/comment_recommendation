def play_ball():
    v, t, s, d = map(int, input().split())
    if d/v >= t and d/v <= s:
        print('No')
    else:
        print('Yes')
play_ball()
