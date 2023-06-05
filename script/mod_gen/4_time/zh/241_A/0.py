def main():
    a = [int(x) for x in input().split()]
    for i in range(3):
        a = [a[x] for x in a]
    print(a[0])

if __name__ == '__main__':
    main()