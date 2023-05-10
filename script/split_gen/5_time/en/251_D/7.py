def main():
    W = int(input())
    if W <= 2:
        print(2)
        print(1, 1)
    else:
        print(W//2 + W%2)
        print(1 + (W%2), *(2 for _ in range(W//2)))
