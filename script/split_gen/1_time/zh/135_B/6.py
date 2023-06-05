def main():
    n = int(input())
    p = list(map(int, input().split()))
    q = sorted(p)
    if p == q:
        print("YES")
    else:
        for i in range(n):
            for j in range(i + 1, n):
                if p[i] > p[j]:
                    p[i], p[j] = p[j], p[i]
                    if p == q:
                        print("YES")
                        return
                    else:
                        p[i], p[j] = p[j], p[i]
        print("NO")
