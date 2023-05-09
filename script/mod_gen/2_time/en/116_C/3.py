def main():
    N = int(input())
    h = [int(x) for x in input().split()]
    ans = 0
    for i in range(1, N):
        if h[i] > h[i - 1]:
            ans += h[i] - h[i - 1]
    print(ans + h[0])

if __name__ == '__main__':
    main()