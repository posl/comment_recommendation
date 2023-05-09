def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = []
    for i in range(n):
        for j in range(i, n):
            b.append(a[j])
            b.sort()
            print(b)
            print(b[len(b)//2])
            b.clear()

if __name__ == '__main__':
    main()