def main():
    n = int(input())
    total = 0
    for i in range(n):
        x, u = input().split()
        x = float(x)
        if u == "JPY":
            total += x
        else:
            total += x * 380000.0
    print(total)
