def main():
    n = int(input())
    x = 1
    y = 1
    ans = 0
    while x * y < n:
        if x == y:
            x += 1
        elif x < y:
            x += 1
        else:
            y += 1
        ans += 1
    print(ans)
