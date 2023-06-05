def main():
    n = int(input())
    a = list(map(int, input().split()))
    m = []
    for i in range(n):
        for j in range(i, n):
            m.append(sorted(a[i:j+1])[int((j-i)/2)])
    print(sorted(m)[int((n*(n+1))/4)])

if __name__ == '__main__':
    main()