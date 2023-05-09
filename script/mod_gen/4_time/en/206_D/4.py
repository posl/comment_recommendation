def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = a[::-1]
    c = []
    for i in range(n):
        if a[i] != b[i]:
            c.append(a[i])
    print(len(c)//2)

if __name__ == '__main__':
    main()