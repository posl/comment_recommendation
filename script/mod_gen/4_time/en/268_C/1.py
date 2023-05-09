def main():
    n = int(input())
    p = list(map(int, input().split()))
    count = 0
    for i in range(n-1):
        if p[i] == i:
            p[i], p[i+1] = p[i+1], p[i]
            count += 1
    if p[-1] == n-1:
        count += 1
    print(count)

if __name__ == '__main__':
    main()