def main():
    L, Q = map(int, input().split())
    x = [0] * Q
    c = [0] * Q
    for i in range(Q):
        c[i], x[i] = map(int, input().split())
    piece = []
    piece.append((1, L))
    for i in range(Q):
        if c[i] == 1:
            for j in range(len(piece)):
                if x[i] >= piece[j][0] and x[i] <= piece[j][1]:
                    piece.append((piece[j][0], x[i]))
                    piece.append((x[i], piece[j][1]))
                    del piece[j]
                    break
        else:
            for j in range(len(piece)):
                if x[i] >= piece[j][0] and x[i] <= piece[j][1]:
                    print(piece[j][1]-piece[j][0])
                    break

if __name__ == '__main__':
    main()