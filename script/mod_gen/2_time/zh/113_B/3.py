def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    ans = 0
    min = float('inf')
    for i in range(n):
        temp = t - h[i] * 0.006
        if abs(temp - a) < min:
            min = abs(temp - a)
            ans = i + 1
    print(ans)

if __name__ == '__main__':
    main()