def main():
    a = input().split()
    a = [int(i) for i in a]
    a.sort()
    print(a[0])

if __name__ == '__main__':
    main()