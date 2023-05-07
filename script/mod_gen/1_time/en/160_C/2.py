def main():
    k, n = map(int, input().split())
    a = list(map(int, input().split()))
    a.append(a[0]+k)
    d = []
    for i in range(n):
        d.append(a[i+1]-a[i])
    print(k-max(d))

if __name__ == '__main__':
    main()