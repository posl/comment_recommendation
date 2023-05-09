def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    c = list(map(int, input().split()))
    ans = -10**18
    for i in range(n):
        x = i
        score = 0
        l = []
        for j in range(k):
            x = p[x]-1
            score += c[x]
            l.append(c[x])
            if x == i:
                break
        if score > 0:
            ans = max(ans, score*(k//(j+1)) + sum(l[0:k%(j+1)]))
        else:
            ans = max(ans, sum(l[0:k]))
    print(ans)
