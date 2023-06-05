def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    ans = 0
    min = 100000
    for i in range(n):
        if abs(min - a) > abs(t - h[i] * 0.006 - a):
            min = t - h[i] * 0.006
            ans = i + 1
    print(ans)

if __name__ == '__main__':
    main()