def main():
    n, a, b = map(int, input().split())
    for i in range(n):
        for j in range(a):
            for k in range(n):
                for l in range(b):
                    print('.' if (i+j)%2 == 0 else '#', end='')
                print(end='')
            print()
        print()

if __name__ == '__main__':
    main()