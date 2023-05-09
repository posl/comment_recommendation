def main():
    n = int(input())
    a = list(map(int, input().split()))
    max = 0
    sum = 0
    for i in range(n):
        sum += a[i]
        if abs(sum) > max:
            max = abs(sum)
    print(max)
main()

if __name__ == '__main__':
    main()