def main():
    n = int(input())
    p = list(map(int, input().split()))
    q = sorted(p)
    if p == q:
        print("YES")
        return
    for i in range(n):
        for j in range(i + 1, n):
            r = p.copy()
            r[i], r[j] = r[j], r[i]
            if r == q:
                print("YES")
                return
    print("NO")
