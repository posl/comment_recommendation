def gold_coins():
    x = int(input())
    if x < 500:
        print(x*2)
    elif x >= 500:
        print((x//500)*1000 + ((x%500)//5)*5)
gold_coins()

if __name__ == '__main__':
    gold_coins()