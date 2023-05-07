def main():
    x = int(input())
    ans = 0
    y = 100
    while y < x:
        y = int(y * 1.01)
        ans += 1
    print(ans)
