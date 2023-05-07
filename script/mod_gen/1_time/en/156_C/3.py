def main():
    n = int(input())
    x = [int(x) for x in input().split()]
    x.sort()
    ans = 0
    for i in range(n):
        ans += (x[i] - x[n//2])**2
    print(ans)

if __name__ == '__main__':
    main()