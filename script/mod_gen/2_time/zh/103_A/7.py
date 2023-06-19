def main():
    a = input().split()
    a = [int(a[i]) for i in range(3)]
    a.sort()
    print(a[2] - a[0])

if __name__ == '__main__':
    main()