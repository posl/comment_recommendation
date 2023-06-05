def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [0]*n
    for i in range(n):
        b[i] = a[i]
        if i == 0:
            print(1)
            continue
        if a[i] == a[i-1]:
            b[i] = 0
        print(len(set(b))-1)

if __name__ == '__main__':
    main()