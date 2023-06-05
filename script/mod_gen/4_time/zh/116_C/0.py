def main():
    N = int(input())
    h = list(map(int, input().split()))
    ans = 0
    while True:
        left = 0
        right = 0
        for i in range(N):
            if h[i] > 0:
                left = i
                break
        for i in range(N-1, -1, -1):
            if h[i] > 0:
                right = i
                break
        if left == right:
            break
        for i in range(left, right+1):
            if h[i] > 0:
                h[i] -= 1
        ans += 1
    print(ans)

if __name__ == '__main__':
    main()