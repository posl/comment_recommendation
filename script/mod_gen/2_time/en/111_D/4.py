def solve():
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]
    if N == 1:
        print(2)
        print(1, 1)
        print("RU")
        print("UR")
        return
    x, y = XY[0]
    if x == 0 and y == 0:
        print(2)
        print(1, 1)
        print("RU")
        print("UR")
        return
    if x == 0:
        print(3)
        print(1, 1, abs(y))
        print("RU" if y > 0 else "RD")
        print("UR" if y > 0 else "DR")
        print("R" if y > 0 else "D")
        return
    if y == 0:
        print(3)
        print(1, 1, abs(x))
        print("RU" if x > 0 else "LU")
        print("UR" if x > 0 else "UL")
        print("U" if x > 0 else "L")
        return
    if x > 0 and y > 0:
        print(4)
        print(1, 1, abs(x), abs(y))
        print("RU")
        print("RU" if x > 0 else "LU")
        print("UR" if x > 0 else "UL")
        print("U" if x > 0 else "L")
        return
    if x > 0 and y < 0:
        print(4)
        print(1, 1, abs(x), abs(y))
        print("RD")
        print("RU" if x > 0 else "LU")
        print("UR" if x > 0 else "UL")
        print("U" if x > 0 else "L")
        return
    if x < 0 and y > 0:
        print(4)
        print(1, 1, abs(x), abs(y))
        print("LU")
        print("RU" if x > 0 else "LU")
        print("UR" if x > 0 else "UL")
        print("U" if x > 0 else "L")
        return
    if x < 0 and y < 0:
        print(

if __name__ == '__main__':
    solve()