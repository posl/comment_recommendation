def main():
    h, w, n = map(int, input().split())
    card = [[0 for _ in range(w)] for _ in range(h)]
    for i in range(n):
        a, b = map(int, input().split())
        card[a-1][b-1] = i+1
    print(card)
    for i in range(h):
        for j in range(w):
            print(card[i][j], end=' ')
        print()
    for i in range(h):
        for j in range(w):
            if card[i][j] == 0:
                card[i].pop(j)
                card[i].append(0)
                break
    print(card)
    for i in range(h):
        for j in range(w):
            print(card[i][j], end=' ')
        print()
    for j in range(w):
        for i in range(h):
            if card[i][j] == 0:
                for k in range(h):
                    card[k][j] = card[k][j+1]
                card[h-1][j] = 0
                break
    print(card)
    for i in range(h):
        for j in range(w):
            print(card[i][j], end=' ')
        print()
    for i in range(h):
        for j in range(w):
            print(card[i][j], end=' ')
        print()

if __name__ == '__main__':
    main()