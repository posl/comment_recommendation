def main():
    n = int(input())
    points = []
    for i in range(n):
        points.append(list(map(int, input().split())))
    if n == 1:
        print(0)
        print(0)
        print(" ")
        print(" ")
    elif n == 2:
        print(1)
        print(abs(points[1][0] - points[0][0]))
        print("L" if points[1][0] < points[0][0] else "R")
        print(" ")
    else:
        print(2)
        print(abs(points[1][0] - points[0][0]))
        print("L" if points[1][0] < points[0][0] else "R")
        print("U" if points[1][1] < points[0][1] else "D")
        print(" ")

if __name__ == '__main__':
    main()