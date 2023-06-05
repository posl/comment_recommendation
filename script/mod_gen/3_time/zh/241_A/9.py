def main():
    a = input()
    a = a.split(' ')
    for i in range(10):
        a[i] = int(a[i])
    k = 0
    for i in range(3):
        k = a[k]
    print(k)

if __name__ == '__main__':
    main()