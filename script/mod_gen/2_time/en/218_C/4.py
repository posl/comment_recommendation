def main():
    n = int(input())
    s = [input() for _ in range(n)]
    t = [input() for _ in range(n)]
    # find top left of s and t
    for i in range(n):
        for j in range(n):
            if s[i][j] == '#':
                s_top = i
                s_left = j
            if t[i][j] == '#':
                t_top = i
                t_left = j
    # find bottom right of s and t
    for i in range(n-1, -1, -1):
        for j in range(n-1, -1, -1):
            if s[i][j] == '#':
                s_bottom = i
                s_right = j
            if t[i][j] == '#':
                t_bottom = i
                t_right = j
    # find height and width of s and t
    s_height = s_bottom - s_top + 1
    s_width = s_right - s_left + 1
    t_height = t_bottom - t_top + 1
    t_width = t_right - t_left + 1
    # check if height and width are same
    if s_height != t_height or s_width != t_width:
        print('No')
        return
    # check if s and t are same after rotation and translation
    for i in range(t_height):
        for j in range(t_width):
            if s[s_top + i][s_left + j] != t[t_top + j][t_right - i]:
                print('No')
                return
    print('Yes')

if __name__ == '__main__':
    main()