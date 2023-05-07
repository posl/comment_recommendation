def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    p = 0
    square = [0, 0, 0, 0]
    for i in range(n):
        square[0] += 1
        square[a[i]] += 1
        if square[1] > 0:
            square[1] -= 1
            p += 1
        if square[2] > 0:
            square[2] -= 1
            p += 1
        if square[3] > 0:
            square[3] -= 1
            p += 1
    print(p)
