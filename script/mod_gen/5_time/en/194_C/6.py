def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(1, n):
        ans += sum([(a[i] - a[j])**2 for j in range(i)])
    print(ans)

if __name__ == '__main__':
    main()