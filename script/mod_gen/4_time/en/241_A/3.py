def main():
    a = input().split()
    b = 0
    for i in range(3):
        b = int(a[b])
    print(b)

if __name__ == '__main__':
    main()