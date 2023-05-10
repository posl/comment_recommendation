def main():
    H, W, N = map(int, input().split())
    cards = [list(map(int, input().split())) for _ in range(N)]
    rows = list(range(1, H+1))
    cols = list(range(1, W+1))
    for card in cards:
        if card[0] in rows:
            rows.remove(card[0])
        if card[1] in cols:
            cols.remove(card[1])
    for i in range(N):
        print(rows[i], cols[i])
