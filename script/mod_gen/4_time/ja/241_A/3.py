def main():
    a = list(map(int, input().split()))
    k = 0
    for i in range(0, 3):
        k = a[k]
    print(k)

if __name__ == '__main__':
    main()