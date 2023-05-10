def main():
    h, w = map(int, input().split())
    s = [list(input()) for i in range(h)]
    #print(s)
    #print(len(s))
    #print(len(s[0]))
    #駒の位置を探す
    for i in range(h):
        for j in range(w):
            if s[i][j] == 'o':
                koma = [i, j]
                #print(koma)
    #移動回数をカウントする
    count = 0
    while True:
        #print(count)
        #print(koma)
        if koma[0] == 0:
            if koma[1] == 0:
                if s[koma[0]][koma[1]+1] == '-':
                    s[koma[0]][koma[1]+1] = 'o'
                    s[koma[0]][koma[1]] = '-'
                    koma[1] += 1
                    count += 1
                else:
                    s[koma[0]+1][koma[1]] = 'o'
                    s[koma[0]][koma[1]] = '-'
                    koma[0] += 1
                    count += 1
            elif koma[1] == w-1:
                if s[koma[0]][koma[1]-1] == '-':
                    s[koma[0]][koma[1]-1] = 'o'
                    s[koma[0]][koma[1]] = '-'
                    koma[1] -= 1
                    count += 1
                else:
                    s[koma[0]+1][koma[1]] = 'o'
                    s[koma[0]][koma[1]] = '-'
                    koma[0] += 1
                    count += 1
            else:
                if s[koma[0]][koma[1]-1] == '-':
                    s[koma[0]][koma[1]-1] = 'o'
                    s[koma[0]][koma[1]] = '-'
                    koma[1] -= 1
                    count += 1
                elif s[koma[0]][koma[1]+1] == '-':
                    s[koma[0]][koma
