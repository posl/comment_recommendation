def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    ans = 0
    diff = 100000000
    for i in range(n):
        tmp = t - h[i] * 0.006
        if diff > abs(a - tmp):
            ans = i + 1
            diff = abs(a - tmp)
    print(ans)

if __name__ == '__main__':
    main()