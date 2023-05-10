def main():
    N, X = map(int, input().split())
    amount = 0
    for i in range(N):
        A, B = map(int, input().split())
        amount += A * B
        if amount > X * 100:
            print("No")
            return
    print("Yes")
