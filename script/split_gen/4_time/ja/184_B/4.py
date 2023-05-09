def main():
    n, x = map(int, input().split())
    s = input()
    ans = x
    for i in s:
        if i == 'o':
            ans += 1
        elif ans > 0:
            ans -= 1
    print(ans)
