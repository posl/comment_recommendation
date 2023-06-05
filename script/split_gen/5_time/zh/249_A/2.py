def main():
    A, B, C, D, E, F, X = map(int, input().split())
    taka = 0
    aoki = 0
    taka_speed = A * B
    aoki_speed = D * E
    for i in range(X):
        if i % (A + C) < A:
            taka += B
        if i % (D + F) < D:
            aoki += E
    if taka > aoki:
        print("高桥")
    elif taka < aoki:
        print("青木")
    else:
        print("画")
