def main():
    # Get input here
    n = int(input())
    a = list(map(int, input().split()))
    # Calculate result here
    ans = 0
    for i in range(n):
        ans += a[i]
    # Print output here
    print(360 - ans)
main()

if __name__ == '__main__':
    main()