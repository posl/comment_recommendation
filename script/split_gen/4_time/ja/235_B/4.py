def main():
    n = int(input())
    h = [int(x) for x in input().split()]
    max_h = 0
    ans = 0
    for i in range(n):
        if max_h <= h[i]:
            ans += 1
            max_h = h[i]
    print(ans)
