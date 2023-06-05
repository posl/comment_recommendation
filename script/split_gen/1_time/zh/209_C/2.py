def main():
    n = int(input())
    c = list(map(int, input().split()))
    c.sort()
    ans = 1
    for i in range(n):
        ans = ans * max(c[i] - i, 0) % (10 ** 9 + 7)
    print(ans)
