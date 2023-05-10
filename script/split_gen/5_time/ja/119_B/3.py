def main():
    n = int(input())
    total = 0
    for i in range(n):
        x, u = input().split()
        if u == 'JPY':
            total += int(x)
        else:
            total += float(x) * 380000.0
    print(total)
