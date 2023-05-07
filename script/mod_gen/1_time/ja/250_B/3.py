def main():
    n, a, b = map(int, input().split())
    for i in range(a):
        for j in range(n):
            for k in range(b):
                for l in range(n):
                    if (i + j + k + l) % 2 == 0:
                        print("#", end="")
                    else:
                        print(".", end="")
            print()
    return

if __name__ == '__main__':
    main()