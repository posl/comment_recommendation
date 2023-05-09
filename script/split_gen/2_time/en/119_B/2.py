def main():
    N = int(input())
    total = 0
    for i in range(N):
        x, u = input().split()
        if u == "JPY":
            total += float(x)
        else:
            total += float(x) * 380000.0
    print(total)
