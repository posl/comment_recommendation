def main():
    #H, W = map(int, input().split())
    #G = [input() for i in range(H)]
    H, W = 9, 44
    G = ['RRDDDDRRRDDDRRRRRRDDDRDDDDRDDRDDDDDDRRDRRRRR',
         'RRRDLRDRDLLLLRDRRLLLDDRDLLLRDDDLLLDRRLLLLLDD',
         'DRDLRLDRDLRDRLDRLRDDLDDLRDRLDRLDDRLRRLRRRDRR',
         'DDLRRDLDDLDDRLDDLDRDDRDDDDRLRRLRDDRRRLDRDRDD',
         'RDLRRDLRDLLLLRRDLRDRRDRRRDLRDDLLLLDDDLLLLRDR',
         'RDLLLLLRDLRDRLDDLDDRDRRDRLDRRRLDDDLDDDRDDLDR',
         'RDLRRDLDDLRDRLRDLDDDLDDRLDRDRDLDRDLDDLRRDLRR',
         'RDLDRRLDRLLLLDRDRLLLRDDLLLLLRDRLLLRRRRLLLDDR',
         'RRRRDRDDRRRDDRDDDRRRDRDRDRDRRRRRRDDDRDDDDRRR']
    i, j = 0, 0
    while True:
        if G[i][j] == 'U' and i != 0:
            i -= 1
        elif G[i][j] == 'D' and i != H - 1:
            i += 1
        elif G[i][j] == 'L' and j != 0:
            j -= 1
        elif G[i][j] == 'R' and j != W - 1:
            j += 1
        else:
            break
    if len(set(G[i][j])) == 1:
        print(-1)
    else:
        print(i + 1, j + 1)
