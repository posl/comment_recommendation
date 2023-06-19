def main():
    a = input().split()
    a = list(map(int, a))
    k = 0
    for i in range(10):
        k = a[k]
    print(k)

if __name__ == '__main__':
    main()