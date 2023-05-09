def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort()
    b = []
    for i in range(n):
        if a[i] not in b:
            b.append(a[i])
    b.sort()
    for i in range(n):
        if b[i] != i:
            print(i)
            break
        elif i == n-1:
            print(n)
main()

if __name__ == '__main__':
    main()