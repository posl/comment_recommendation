def main():
    n = int(input())
    d = {}
    for i in range(n):
        s = input()
        s = sorted(s)
        s = ''.join(s)
        if s in d:
            d[s] += 1
        else:
            d[s] = 1
    ans = 0
    for i in d.values():
        ans += i * (i - 1) // 2
    print(ans)
