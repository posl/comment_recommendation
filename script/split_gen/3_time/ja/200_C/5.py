def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [a % 200 for a in A]
    from collections import Counter
    c = Counter(A)
    ans = 0
    for v in c.values():
        ans += v * (v - 1) // 2
    print(ans)
