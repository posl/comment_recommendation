def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    H = [T - h * 0.006 for h in H]
    min_diff = 100
    for i, h in enumerate(H):
        if abs(A - h) < min_diff:
            min_diff = abs(A - h)
            ans = i + 1
    print(ans)

if __name__ == '__main__':
    main()