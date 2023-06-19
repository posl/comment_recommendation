def main():
    n = int(input())
    sum = 0
    for i in range(n):
        x, u = input().split()
        if u == 'BTC':
            sum += 380000.0 * float(x)
        else:
            sum += float(x)
    print(sum)
