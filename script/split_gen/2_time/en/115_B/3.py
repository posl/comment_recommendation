def main():
    num = int(input())
    prices = []
    for i in range(num):
        prices.append(int(input()))
    prices.sort(reverse=True)
    total = 0
    for i in range(num):
        if i == 0:
            total += (prices[i] / 2)
        else:
            total += prices[i]
    print(int(total))
