def main():
    n = int(input())
    a = list(map(int, input().split()))
    maxa = 0
    sum = 0
    for i in range(n):
        sum += a[i]
        if sum > maxa:
            maxa = sum
    print(maxa)

if __name__ == '__main__':
    main()