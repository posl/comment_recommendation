def main():
    k, n = map(int, input().split())
    a = list(map(int, input().split()))
    a.append(a[0]+k)
    max_d = 0
    for i in range(n):
        d = a[i+1]-a[i]
        if d > max_d:
            max_d = d
    print(k-max_d)

if __name__ == '__main__':
    main()