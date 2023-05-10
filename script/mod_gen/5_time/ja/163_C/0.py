def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = [0] * n
    for i in range(1, n):
        ans[a[i-1]-1] += 1
    for i in range(n):
        print(ans[i])

if __name__ == '__main__':
    main()