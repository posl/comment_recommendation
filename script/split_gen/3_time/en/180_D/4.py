def main():
    x, y, a, b = map(int, input().split())
    ans = 0
    while x < y:
        if x * a < x + b:
            if x * a < y:
                x *= a
                ans += 1
            else:
                break
        else:
            ans += (y - x - 1) // b
            break
    print(ans)
