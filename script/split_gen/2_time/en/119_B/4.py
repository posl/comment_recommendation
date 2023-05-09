def main():
    N = int(input())
    Y = 0
    for i in range(N):
        x, u = input().split()
        x = float(x)
        if u == 'JPY':
            Y += x
        else:
            Y += x*380000.0
    print(Y)
