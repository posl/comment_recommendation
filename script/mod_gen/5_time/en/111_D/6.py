def solve():
    n = int(input())
    points = [tuple(map(int, input().split())) for _ in range(n)]
    if n == 1:
        print(0)
        print()
        print()
        return
    if n == 2:
        print(1)
        print(1)
        print("L" if points[0][0] > points[1][0] else "R")
        return
    if n == 3:
        print(2)
        print(1, 1)
        print("RU" if points[0][0] > points[1][0] else "UR")
        print("RU" if points[1][0] > points[2][0] else "UR")
        return
    print(5)
    print(3, 1, 4, 1, 5)
    print("L" * 3 + "U" * 3 + "R" * 3 + "D" * 3 + "L" * 3)
    print("L" * 3 + "D" * 3 + "R" * 3 + "U" * 3 + "L" * 3)
    print("R" * 3 + "U" * 3 + "L" * 3 + "D" * 3 + "R" * 3)
    print("R" * 3 + "D" * 3 + "L" * 3 + "U" * 3 + "R" * 3)
    print("L" * 3 + "U" * 3 + "R" * 3 + "D" * 3 + "L" * 3)
    return
solve()

if __name__ == '__main__':
    solve()