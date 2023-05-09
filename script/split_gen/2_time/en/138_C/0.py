def main():
    n = int(input())
    v = list(map(int, input().split()))
    v.sort()
    ans = (v[0] + v[1]) / 2
    for i in range(2, n):
        ans = (ans + v[i]) / 2
    print(ans)
