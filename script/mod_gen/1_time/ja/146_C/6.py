def main():
    A, B, X = map(int, input().split())
    max = 0
    for i in range(1, 10):
        if (A * (10 ** (i - 1)) + B * i) <= X:
            max = 10 ** (i - 1)
    if A * max + B * len(str(max)) <= X:
        print(max * 10 + (X - (A * max + B * len(str(max)))) // A)
    else:
        print(max)

if __name__ == '__main__':
    main()