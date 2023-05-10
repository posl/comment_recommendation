def main():
    n = int(input())
    p = list(map(int, input().split()))
    count = 0
    min = n
    for i in range(n):
        if p[i] <= min:
            count += 1
            min = p[i]
    print(count)

if __name__ == '__main__':
    main()