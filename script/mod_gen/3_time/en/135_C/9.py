def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = []
    for i in range(n):
        c.append(min(b[i], a[i]))
        c.append(min(b[i+1], a[i]-c[i]))
    print(sum(c))

if __name__ == '__main__':
    main()