def main():
    x = input()
    m = int(input())
    d = int(max(x))
    l = len(x)
    if l == 1:
        print(0 if int(x) > m else 1)
        return
    ans = 0
    for i in range(d+1, 10):
        if int(str(i) * l) <= m:
            ans += 1
    for i in range(1, l):
        ans += 9 * 10 ** (i-1)
    print(ans)
