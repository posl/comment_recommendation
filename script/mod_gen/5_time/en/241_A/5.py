def main():
    a = input()
    a = a.split()
    a = [int(i) for i in a]
    k = 0
    for i in range(3):
        k = a[k]
    print(k)

if __name__ == '__main__':
    main()