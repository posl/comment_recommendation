def main():
    p = int(input())
    n = 10
    coin = []
    for i in range(1, n+1):
        coin.append(i)
    coin.reverse()
    count = 0
    for i in range(n):
        count += p // coin[i]
        p = p % coin[i]
    print(count)
