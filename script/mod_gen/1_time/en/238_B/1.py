def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.reverse()
    angle = 0
    for a in A:
        angle += a
        angle %= 360
    angle = 360 - angle
    angle %= 360
    print(angle)
main()

if __name__ == '__main__':
    main()