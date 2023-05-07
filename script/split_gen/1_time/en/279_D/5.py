def main():
    a, b = map(int, input().split())
    ans = 0
    if a <= b:
        ans = a
    else:
        ans = a / ((2) ** (1 / 2))
        if ans > b:
            ans = a / ((3) ** (1 / 2))
    print(ans)
