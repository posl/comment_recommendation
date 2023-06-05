def main():
    x = int(input())
    ans = 0
    ans += 1000 * (x // 500)
    ans += 5 * ((x % 500) // 5)
    print(ans)
