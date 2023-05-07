def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    T = [input() for _ in range(H)]
    if H == 1 and W == 1:
        if S[0] == T[0]:
            print('Yes')
        else:
            print('No')
        return
    if H == 1:
        for i in range(W):
            if S[0][i] == '#':
                for j in range(W):
                    if T[0][j] == '#':
                        if S[0][i:] + S[0][:i] == T[0][j:] + T[0][:j]:
                            print('Yes')
                            return
        print('No')
        return
    if W == 1:
        for i in range(H):
            if S[i][0] == '#':
                for j in range(H):
                    if T[j][0] == '#':
                        if S[i:] + S[:i] == T[j:] + T[:j]:
                            print('Yes')
                            return
        print('No')
        return
    for i in range(H):
        if S[i][0] == '#':
            for j in range(H):
                if T[j][0] == '#':
                    if S[i:] + S[:i] == T[j:] + T[:j]:
                        for k in range(W):
                            if S[i][k] == '#':
                                for l in range(W):
                                    if T[j][l] == '#':
                                        if S[i][k:] + S[i][:k] == T[j][l:] + T[j][:l]:
                                            print('Yes')
                                            return
    print('No')
