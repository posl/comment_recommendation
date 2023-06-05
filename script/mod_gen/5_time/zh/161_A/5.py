def main():
    a = input().split()
    a = list(map(int, a))
    a.sort()
    print(a[0], a[1], a[2])

if __name__ == '__main__':
    main()