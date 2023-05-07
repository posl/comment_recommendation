def main():
    a = list(map(int, input().split()))
    for i in range(3):
        a = [a[a[0]]] + a[1:]
    print(a[0])

if __name__ == '__main__':
    main()