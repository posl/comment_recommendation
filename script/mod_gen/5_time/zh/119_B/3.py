def main():
    n = int(input())
    sum = 0
    for i in range(n):
        a, b = input().split()
        if b == 'BTC':
            sum += float(a) * 380000
        else:
            sum += float(a)
    print(sum)
main()
