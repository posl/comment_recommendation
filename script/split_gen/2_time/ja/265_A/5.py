def main():
    x, y, n = map(int, input().split())
    #print(x, y, n)
    apple = 0
    money = 0
    while apple < n:
        if (n - apple) % 3 == 0:
            money += y
            apple += 3
        else:
            money += x
            apple += 1
    print(money)
