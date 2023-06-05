def main():
    n = int(input())
    sum = 0
    for i in range(n):
        x, u = input().split()
        if u == 'BTC':
            x = float(x)
            x = x * 380000
        else:
            x = int(x)
        sum += x
    print(sum)
