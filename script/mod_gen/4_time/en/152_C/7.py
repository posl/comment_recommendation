def main():
    n = int(input())
    p = list(map(int, input().split()))
    count = 0
    min_value = n
    for i in range(n):
        if min_value > p[i]:
            min_value = p[i]
            count += 1
    print(count)

if __name__ == '__main__':
    main()