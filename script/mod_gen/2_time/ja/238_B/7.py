def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a.append(a[0])
    max = 0
    for i in range(n):
        if max < a[i+1] - a[i]:
            max = a[i+1] - a[i]
    print(360 - max)

if __name__ == '__main__':
    main()