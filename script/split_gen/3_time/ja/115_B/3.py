def main():
    n = int(input())
    price = []
    for i in range(n):
        price.append(int(input()))
    price.sort()
    price[-1] = price[-1] // 2
    print(sum(price))
