def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    drinks = []
    for i in range(N):
        drinks.append([A[i], B[i]])
    drinks.sort()
    price = 0
    num = M
    for i in range(N):
        if num >= drinks[i][1]:
            price += drinks[i][0] * drinks[i][1]
            num -= drinks[i][1]
        else:
            price += drinks[i][0] * num
            break
    print(price)
