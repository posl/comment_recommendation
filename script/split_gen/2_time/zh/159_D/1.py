def main():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = [0] * (N + 1)
    for a in A:
        cnt[a] += 1
    ans = sum([c * (c - 1) // 2 for c in cnt])
    for a in A:
        print(ans - (cnt[a] - 1))
