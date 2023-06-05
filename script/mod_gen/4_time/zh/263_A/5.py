def main():
    a = input().split()
    if a.count(a[0]) == 3 and a.count(a[1]) == 2:
        print('Yes')
    elif a.count(a[0]) == 2 and a.count(a[1]) == 3:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()