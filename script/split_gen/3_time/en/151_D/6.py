def main():
    h, w = map(int, input().split())
    s = [list(input()) for i in range(h)]
    max_move = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '.':
                max_move = max(max_move, max_move_from(i, j, s))
    print(max_move)
