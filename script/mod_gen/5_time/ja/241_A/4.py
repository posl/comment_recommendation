def main():
    a = list(map(int, input().split()))
    #print(a)
    count = 0
    while True:
        if a[count] == 0:
            break
        count = a[count]
    print(count)

if __name__ == '__main__':
    main()