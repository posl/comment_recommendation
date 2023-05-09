def main():
    import math
    x, y, r = map(float, input().split())
    x = x * 10000
    y = y * 10000
    r = r * 10000
    x = round(x)
    y = round(y)
    r = round(r)
    ans = 0
    for i in range(-100000, 100001):
        if x - r > i * 10000:
            continue
        if x + r < i * 10000:
            break
        tmp = math.sqrt(r ** 2 - (i * 10000 - x) ** 2)
        ans += int((y + tmp) / 10000) - int((y - tmp) / 10000) + 1
    print(ans)
