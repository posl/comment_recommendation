def main():
    n = int(input())
    a = list(range(1, 2*n+2))
    for i in range(n):
        print(a[i])
        input()
        print(a[-i-1])
        input()
    print(a[n])
    input()

if __name__ == '__main__':
    main()