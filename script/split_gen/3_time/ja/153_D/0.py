def main():
    h = int(input())
    ans = 0
    while h > 0:
        ans += h
        h //= 2
    print(ans)
