def main():
    h, w = map(int, input().split())
    a = [input() for _ in range(h)]
    #print(a)
    h_list = [False] * h
    w_list = [False] * w
    #print(h_list)
    #print(w_list)
    for i in range(h):
        for j in range(w):
            if a[i][j] == '#':
                h_list[i] = True
                w_list[j] = True
    #print(h_list)
    #print(w_list)
    for i in range(h):
        if h_list[i]:
            for j in range(w):
                if w_list[j]:
                    print(a[i][j], end='')
            print()
