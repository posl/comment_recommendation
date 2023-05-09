def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(1, n):
        p1 = p[i-1]
        p2 = p[i]
        if p1 > p2:
            p1, p2 = p2, p1
        if p2 == n:
            ans = i
            break
    print(ans)
