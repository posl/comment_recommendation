def main():
    n = int(input())
    t, a = map(int,input().split())
    h = list(map(int,input().split()))
    ans = 0
    min = 100000000
    for i in range(0,n):
        if min > abs(a - (t - h[i] * 0.006)):
            min = abs(a - (t - h[i] * 0.006))
            ans = i + 1
    print(ans)

if __name__ == '__main__':
    main()