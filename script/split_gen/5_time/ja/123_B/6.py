def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    ans = 0
    ans += (a // 10) * 10
    if a % 10 != 0:
        ans += 10
    ans += (b // 10) * 10
    if b % 10 != 0:
        ans += 10
    ans += (c // 10) * 10
    if c % 10 != 0:
        ans += 10
    ans += (d // 10) * 10
    if d % 10 != 0:
        ans += 10
    ans += (e // 10) * 10
    if e % 10 != 0:
        ans += 10
    print(ans)
