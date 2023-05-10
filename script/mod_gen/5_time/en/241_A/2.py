def main():
    a = list(map(int, input().split()))
    i = 0
    while True:
        if a[i] == 0:
            print(i)
            break
        i = a[i]

if __name__ == '__main__':
    main()