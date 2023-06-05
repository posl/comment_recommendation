def main():
    a = map(int, raw_input().split())
    for i in range(10):
        a[i] = a[a[i]]
    print a[0]

if __name__ == '__main__':
    main()