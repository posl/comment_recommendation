def main():
    n = int(input())
    h = list(map(int, input().split()))
    l = []
    for i in range(n):
        l.append(h[i])
        if i > 0 and h[i] <= h[i-1]:
            l.append(0)
    print(max(l))

if __name__ == '__main__':
    main()