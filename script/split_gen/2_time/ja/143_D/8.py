def main():
    n = int(input())
    l = list(map(int, input().split()))
    l = sorted(l)
    ans = 0
    for a in range(n):
        for b in range(a+1, n):
            for c in range(b+1, n):
                if l[a] == l[b] or l[b] == l[c] or l[c] == l[a]:
                    continue
                if l[a] + l[b] > l[c]:
                    ans += 1
    print(ans)
