def main():
    H, W = map(int, input().split())
    S = [input() for i in range(H)]
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                if i == 0:
                    print('4')
                    return
                if i == H-1:
                    print('4')
                    return
                if j == 0:
                    print('4')
                    return
                if j == W-1:
                    print('4')
                    return
                if i-1 >= 0:
                    if S[i-1][j] == '.':
                        print('4')
                        return
                if i+1 <= H-1:
                    if S[i+1][j] == '.':
                        print('4')
                        return
                if j-1 >= 0:
                    if S[i][j-1] == '.':
                        print('4')
                        return
                if j+1 <= W-1:
                    if S[i][j+1] == '.':
                        print('4')
                        return
    print('3')
