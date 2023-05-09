def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        ans |= a[i]
    print(ans ^ a[0])

if __name__ == '__main__':
    main()