def main():
    y = int(input())
    ans = y
    while ans % 4 != 2:
        ans += 1
    print(ans)
