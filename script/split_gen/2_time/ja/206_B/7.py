def main():
    N = int(input())
    #貯金箱の中身
    box = 0
    #貯金箱に入れた金額
    money = 0
    #何日目か
    day = 0
    while box < N:
        day += 1
        money += day
        box += money
    print(day)
