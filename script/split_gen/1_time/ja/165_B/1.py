def main():
    x = int(input())
    money = 100
    cnt = 0
    while money < x:
        money = int(money * 1.01)
        cnt += 1
    print(cnt)
