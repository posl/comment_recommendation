def main():
    n = int(input())
    total = 0
    for i in range(n):
        x, u = input().split()
        if u == 'BTC':
            total += float(x) * 380000.0
        else:
            total += int(x)
    print(total)
