def main():
    N = int(input())
    BTC = 380000.0
    total = 0
    for i in range(N):
        x, u = input().split()
        x = float(x)
        if u == 'JPY':
            total += x
        else:
            total += x * BTC
    print(total)
