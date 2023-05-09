def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    t = [a, b, c, d, e]
    t.sort()
    ans = 0
    for i in range(4):
        if t[i] % 10 != 0:
            ans += (t[i] // 10 + 1) * 10
        else:
            ans += t[i]
    ans += t[4]
    print(ans)
