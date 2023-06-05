def light_num(H, W, S):
    light = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                continue
            else:
                light += 1
                k = i + 1
                while k < H:
                    if S[k][j] == '.':
                        light += 1
                    else:
                        break
                    k += 1
                k = i - 1
                while k >= 0:
                    if S[k][j] == '.':
                        light += 1
                    else:
                        break
                    k -= 1
                k = j + 1
                while k < W:
                    if S[i][k] == '.':
                        light += 1
                    else:
                        break
                    k += 1
                k = j - 1
                while k >= 0:
                    if S[i][k] == '.':
                        light += 1
                    else:
                        break
                    k -= 1
    return light

if __name__ == '__main__':
    light_num()