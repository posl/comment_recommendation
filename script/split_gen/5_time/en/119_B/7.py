def main():
    N = int(input())
    total = 0
    for i in range(N):
        x,u = input().split()
        x = float(x)
        if u == 'BTC':
            total += x * 380000.0
        else:
            total += x
    print(total)
