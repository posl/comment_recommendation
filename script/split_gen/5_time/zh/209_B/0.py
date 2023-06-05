def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    price = 0
    for i in range(N):
        if i % 2 == 0:
            price += A[i]
        else:
            price += A[i] - 1
    if price <= X:
        print("Yes")
    else:
        print("No")
