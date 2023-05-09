def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    BC = [list(map(int, input().split())) for _ in range(Q)]
    cnt = [0] * (10**5 + 1)
    for a in A:
        cnt[a] += 1
    S = sum(A)
    for b, c in BC:
        S += (c - b) * cnt[b]
        cnt[c] += cnt[b]
        cnt[b] = 0
        print(S)

if __name__ == '__main__':
    main()