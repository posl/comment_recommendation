def main():
    n = int(input())
    L = []
    R = []
    for i in range(n):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    L.sort()
    R.sort()
    ans = 0
    for i in range(n):
        if i == 0 or L[i] > R[i - 1]:
            ans += 1
    print(ans)
