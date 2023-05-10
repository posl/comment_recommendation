def main():
    H, W, C = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    ans = float('inf')
    for h in range(H):
        for w in range(W):
            for hh in range(h, H):
                for ww in range(w, W):
                    if h == hh and w == ww:
                        continue
                    ans = min(ans, A[h][w] + A[hh][ww] + C * (abs(h - hh) + abs(w - ww)))
    print(ans)
