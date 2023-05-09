def main():
    n = int(input())
    a = list(map(int,input().split()))
    ans = 360
    for i in range(n):
        ans = min(ans, abs(360 - 2*sum(a[:i+1])))
    print(ans)

if __name__ == '__main__':
    main()