def main():
    A, B, C = map(int, input().split())
    if A == 0 and B == 0:
        print(99)
        return
    if A == 0 and C == 0:
        print(99)
        return
    if B == 0 and C == 0:
        print(99)
        return
    print(1 + A / (A + B + C) * (1 + B / (A + B + C - 1) * (1 + C / (A + B + C - 2))) + B / (A + B + C) * (1 + A / (A + B + C - 1) * (1 + C / (A + B + C - 2))) + C / (A + B + C) * (1 + A / (A + B + C - 1) * (1 + B / (A + B + C - 2))))
main()

if __name__ == '__main__':
    main()