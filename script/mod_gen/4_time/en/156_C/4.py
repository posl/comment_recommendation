def main():
    n = int(input())
    x = list(map(int, input().split()))
    ans = 10**9
    for i in range(1, 101):
        ans = min(ans, sum([(j - i)**2 for j in x]))
    print(ans)

if __name__ == '__main__':
    main()