def main():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    ans = 0
    for h in range(H):
        for w in range(W):
            if S[h][w] == ".":
                S[h][w] = 0
            else:
                S[h][w] = -1
    for h in range(H):
        for w in range(W):
            if S[h][w] == -1:
                continue
            else:
                if h == 0 and w == 0:
                    continue
                elif h == 0:
                    if S[h][w-1] == -1:
                        S[h][w] = 0
                    else:
                        S[h][w] = S[h][w-1] + 1
                elif w == 0:
                    if S[h-1][w] == -1:
                        S[h][w] = 0
                    else:
                        S[h][w] = S[h-1][w] + 1
                else:
                    if S[h-1][w] == -1 and S[h][w-1] == -1:
                        S[h][w] = 0
                    elif S[h-1][w] == -1:
                        S[h][w] = S[h][w-1] + 1
                    elif S[h][w-1] == -1:
                        S[h][w] = S[h-1][w] + 1
                    else:
                        S[h][w] = min(S[h-1][w], S[h][w-1]) + 1
    print(S[H-1][W-1])
