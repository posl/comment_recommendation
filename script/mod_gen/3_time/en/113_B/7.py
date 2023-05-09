def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    ans = 0
    min = 10**10
    for i in range(n):
        if abs(t-h[i]*0.006-a) < min:
            ans = i+1
            min = abs(t-h[i]*0.006-a)
    print(ans)

if __name__ == '__main__':
    main()