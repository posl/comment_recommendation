def main():
    x, y, r = map(float, input().split())
    x = int(x * 1000)
    y = int(y * 1000)
    r = int(r * 1000)
    ans = 0
    for i in range(-r, r + 1):
        for j in range(-r, r + 1):
            if i * i + j * j <= r * r:
                if x + i >= 0 and x + i <= 100000 and y + j >= 0 and y + j <= 100000:
                    ans += 1
    print(ans)
    return
