def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    min = 0
    for i in range(n):
        if a[i] > min:
            break
        min += a[i]
    print(min)

if __name__ == '__main__':
    main()