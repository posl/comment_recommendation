def main():
    x = int(input())
    ans = 0
    money = 100
    while money < x:
        ans += 1
        money = int(money * 1.01)
    print(ans)
