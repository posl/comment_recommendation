def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    ans = 0
    min_diff = float("inf")
    for i, h in enumerate(H):
        temp = T - h * 0.006
        diff = abs(temp - A)
        if diff < min_diff:
            min_diff = diff
            ans = i + 1
    print(ans)

if __name__ == '__main__':
    main()