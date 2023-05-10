def main():
    n = int(input())
    x = list(map(int, input().split()))
    sum = 0
    for i in range(n):
        sum += x[i]
    avg = round(sum/n)
    ans = 0
    for i in range(n):
        ans += (x[i] - avg)**2
    print(ans)

if __name__ == '__main__':
    main()