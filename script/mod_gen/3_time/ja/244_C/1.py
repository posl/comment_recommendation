def main():
    n = int(input())
    for i in range(1, n+1):
        print(i)
        a = int(input())
        if a == 0:
            return
        print(n+i)
        b = int(input())
        if b == 0:
            return
    print(n+1)
    int(input())
main()

if __name__ == '__main__':
    main()