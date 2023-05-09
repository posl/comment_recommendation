def main():
    n = int(input())
    p = list(map(int, input().split()))
    count = 0
    for i in range(1, n-1):
        a = p[i-1]
        b = p[i]
        c = p[i+1]
        if b == sorted([a, b, c])[1]:
            count += 1
    print(count)

if __name__ == '__main__':
    main()