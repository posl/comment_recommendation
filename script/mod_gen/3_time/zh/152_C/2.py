def main():
    n = int(input())
    p = list(map(int, input().split()))
    min = p[0]
    count = 1
    for i in range(1, n):
        if p[i] < min:
            min = p[i]
            count += 1
    print(count)

if __name__ == '__main__':
    main()