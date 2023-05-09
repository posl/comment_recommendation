def main():
    n, m = map(int, input().split())
    if m == 1:
        for i in range(n):
            for j in range(n):
                print(i+j)
            print()
    else:
        for i in range(n):
            for j in range(n):
                if i == 0 and j == 0:
                    print(0, end="")
                else:
                    print(-1, end="")
                if j < n-1:
                    print(" ", end="")
            print()

if __name__ == '__main__':
    main()