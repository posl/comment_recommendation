def main():
    N = input()
    max = 0
    for i in range(1, len(N)):
        a = int(N[:i])
        b = int(N[i:])
        if a * b > max:
            max = a * b
    print(max)

if __name__ == '__main__':
    main()