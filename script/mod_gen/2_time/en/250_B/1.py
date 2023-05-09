def main():
    n, a, b = map(int, input().split())
    for i in range(a):
        for j in range(n):
            for k in range(b):
                if ((i + j) % 2 == 0):
                    print('.', end='')
                else:
                    print('#', end='')
            if (j != n - 1):
                print('.', end='')
        print()

if __name__ == '__main__':
    main()