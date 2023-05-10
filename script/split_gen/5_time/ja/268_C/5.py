def main():
    n = int(input())
    p = [int(x) for x in input().split()]
    ans = 0
    for i in range(n):
        if i == p[p[i]]:
            ans += 1
    print(ans)
