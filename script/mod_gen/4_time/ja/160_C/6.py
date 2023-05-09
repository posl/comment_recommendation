def main():
    k, n = map(int, input().split())
    a = list(map(int, input().split()))
    a.append(a[0]+k)
    max = 0
    for i in range(n):
        if max < a[i+1] - a[i]:
            max = a[i+1] - a[i]
    print(k - max)

if __name__ == '__main__':
    main()