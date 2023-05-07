def main():
    #入力
    h, w = map(int, input().split())
    g = [input() for _ in range(h)]
    #print(h, w)
    #print(g)
    #処理
    x = 0
    y = 0
    for i in range(10**5):
        if g[x][y] == "U":
            if x == 0:
                break
            else:
                x -= 1
        elif g[x][y] == "D":
            if x == h-1:
                break
            else:
                x += 1
        elif g[x][y] == "L":
            if y == 0:
                break
            else:
                y -= 1
        elif g[x][y] == "R":
            if y == w-1:
                break
            else:
                y += 1
        else:
            print("Error")
    else:
        print("-1")
        return
    #出力
    print(x+1, y+1)

if __name__ == '__main__':
    main()