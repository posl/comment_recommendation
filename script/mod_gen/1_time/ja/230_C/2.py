def main():
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())
    for i in range(P, Q + 1):
        for j in range(R, S + 1):
            if (j - R) % 2 == 0:
                if (i - j + A - B) % 2 == 0 or (i - j + A - B) % 4 == 3:
                    print("#", end="")
                else:
                    print(".", end="")
            else:
                if (i - j + A - B) % 2 == 0 or (i - j + A - B) % 4 == 1:
                    print("#", end="")
                else:
                    print(".", end="")
        print()

if __name__ == '__main__':
    main()