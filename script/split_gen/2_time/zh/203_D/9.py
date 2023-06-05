def main():
    n,k = map(int,input().split())
    money = 0
    for i in range(n):
        a,b = map(int,input().split())
        if k >= a - money:
            k = k - (a - money) + b
            money = a
        else:
            print(money + k)
            exit()
    print(money + k)
