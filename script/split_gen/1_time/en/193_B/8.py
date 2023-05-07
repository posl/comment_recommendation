def main():
    N = int(input())
    min_price = -1
    for n in range(N):
        A, P, X = map(int, input().split())
        if X - A > 0:
            if min_price == -1:
                min_price = P
            elif min_price > P:
                min_price = P
    print(min_price)
