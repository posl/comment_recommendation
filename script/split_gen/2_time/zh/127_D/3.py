def main():
    n, m = map(int, input().split())
    l = 0
    r = n
    for i in range(m):
        ll, rr = map(int, input().split())
        l = max(l, ll)
        r = min(r, rr)
    print(max(0, r - l + 1))
