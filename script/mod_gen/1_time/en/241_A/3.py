def main():
    a = [int(i) for i in input().split()]
    for i in range(3):
        a = [a[j] for j in range(10) if j != a[j]]
    print(a[0])

if __name__ == '__main__':
    main()