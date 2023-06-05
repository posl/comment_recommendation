def get_chess_num():
    h, w = map(int, input().split())
    chess_num = 0
    for i in range(h):
        s = input()
        for j in range(w):
            if s[j] == '#':
                chess_num += 1
    return chess_num
