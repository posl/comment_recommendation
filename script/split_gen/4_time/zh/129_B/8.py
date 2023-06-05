def main():
    n = int(input())
    w = [int(x) for x in input().split()]
    ans = 10000
    for t in range(1, n):
        s1 = sum(w[:t])
        s2 = sum(w[t:])
        if abs(s1-s2) < ans:
            ans = abs(s1-s2)
    print(ans)
