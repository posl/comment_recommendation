def main():
    n = int(input())
    sx, sy, tx, ty = map(int, input().split())
    circles = [list(map(int, input().split())) for _ in range(n)]
    #print(n)
    #print(sx, sy, tx, ty)
    #print(circles)
    # すべての円周上にあるかどうか
    for circle in circles:
        x, y, r = circle
        if (sx - x) ** 2 + (sy - y) ** 2 >= r ** 2 and (tx - x) ** 2 + (ty - y) ** 2 >= r ** 2:
            continue
        else:
            print('No')
            exit()
    # すべての円周上にあるかどうか
    for circle in circles:
        x, y, r = circle
        if (sx - x) ** 2 + (sy - y) ** 2 < r ** 2 and (tx - x) ** 2 + (ty - y) ** 2 < r ** 2:
            continue
        else:
            print('Yes')
            exit()
    print('No')

if __name__ == '__main__':
    main()