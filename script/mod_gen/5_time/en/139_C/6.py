def main():
    n = int(input())
    h = list(map(int, input().split()))
    count = 0
    maxcount = 0
    for i in range(n-1):
        if h[i] >= h[i+1]:
            count += 1
        else:
            if maxcount < count:
                maxcount = count
            count = 0
    if maxcount < count:
        maxcount = count
    print(maxcount)

if __name__ == '__main__':
    main()