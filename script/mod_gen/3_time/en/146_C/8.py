def main():
    A,B,X = list(map(int, input().split()))
    if A > X:
        print(0)
        return
    if A == X:
        print(1)
        return
    if X >= A + B * 10:
        print(10 ** 9)
        return
    for i in range(1, 10):
        if A * (10 ** i) + B * (i + 1) > X:
            print(10 ** (i - 1))
            return
main()

if __name__ == '__main__':
    main()