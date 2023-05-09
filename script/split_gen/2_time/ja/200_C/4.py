def main():
    N = int(input())
    A = list(map(int, input().split()))
    from collections import Counter
    C = Counter([a%200 for a in A])
    ans = 0
    for c in C.values():
        ans += c*(c-1)//2
    print(ans)
