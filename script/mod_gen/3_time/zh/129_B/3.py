def search(n):
    w = list(map(int, input().split()))
    w.sort()
    s1 = 0
    s2 = sum(w)
    ans = s2
    for i in range(n):
        s1 += w[i]
        s2 -= w[i]
        ans = min(ans, abs(s1-s2))
    return ans

if __name__ == '__main__':
    search()