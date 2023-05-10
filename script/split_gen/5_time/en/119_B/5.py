def main():
    N = int(input())
    sum = 0
    for i in range(N):
        x, u = input().split()
        if u == "JPY":
            sum += float(x)
        else:
            sum += float(x)*380000.0
    print(sum)
