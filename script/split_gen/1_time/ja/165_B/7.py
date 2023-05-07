def main():
    X = int(input())
    money = 100
    i = 1
    while True:
        money = money + int(money * 0.01)
        if money >= X:
            break
        i += 1
    print(i)
