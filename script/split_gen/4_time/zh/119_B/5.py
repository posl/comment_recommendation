def main():
    N = int(input())
    sum = 0
    for i in range(N):
        x, u = input().split()
        if u == 'BTC':
            sum += float(x) * 380000
        else:
            sum += int(x)
    print(sum)
