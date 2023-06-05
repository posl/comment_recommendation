def main():
    a = input().split()
    if a[0] == a[1]:
        print(a[2])
    elif a[0] == a[2]:
        print(a[1])
    elif a[1] == a[2]:
        print(a[0])
    else:
        print(0)

if __name__ == '__main__':
    main()