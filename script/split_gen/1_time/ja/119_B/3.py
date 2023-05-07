def main():
    n = int(input())
    y = 0
    for i in range(n):
        x, u = input().split()
        x = float(x)
        if u == "JPY":
            y += x
        else:
            y += x * 380000.0
    print(y)
