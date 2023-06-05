def main():
    a = list(map(int, input().split()))
    for i in range(10):
        if a[0] == a[i]:
            print(i)
            break

if __name__ == '__main__':
    main()