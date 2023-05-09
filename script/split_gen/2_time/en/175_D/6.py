def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    c = list(map(int, input().split()))
    ans = -10**9
    for i in range(n):
        s = 0
        j = i
        for _ in range(k):
            j = p[j]-1
            s += c[j]
            if j == i:
                break
        if s > 0:
            ans = max(ans, s*((k-1)//(j-i+1))+max(sum(c[i:j+1]) for i, j in ((i, i+(k-1)%(j-i+1)) for i in range(j+1))))
        else:
            ans = max(ans, max(sum(c[i:j+1]) for i, j in ((i, i+(k-1)%(j-i+1)) for i in range(j+1))))
    print(ans)
