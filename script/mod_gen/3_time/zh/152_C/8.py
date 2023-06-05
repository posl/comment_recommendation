def main():
    n = int(input())
    p = list(map(int, input().split()))
    count = 0
    min = n + 1
    for i in range(n):
        if p[i] < min:
            min = p[i]
            count += 1
    print(count)

if __name__ == '__main__':
    main()