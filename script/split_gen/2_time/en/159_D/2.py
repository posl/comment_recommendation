def main():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = [0] * (N+1)
    for a in A:
        cnt[a] += 1
    total = 0
    for c in cnt:
        if c > 1:
            total += c * (c-1) // 2
    for a in A:
        print(total - (cnt[a] - 1))
