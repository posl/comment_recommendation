def main():
    N = int(input())
    X = []
    U = []
    for i in range(N):
        x, u = input().split()
        X.append(float(x))
        U.append(u)
    sum = 0.0
    for i in range(N):
        if U[i] == 'JPY':
            sum += X[i]
        else:
            sum += X[i] * 380000.0
    print(sum)
