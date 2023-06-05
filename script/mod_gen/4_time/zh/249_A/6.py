def run():
    A, B, C, D, E, F, X = map(int, input().split())
    taka = 0
    aoki = 0
    for i in range(X):
        if i % (A+B) < A:
            taka += 1
        if i % (D+E) < D:
            aoki += 1
    if taka > aoki:
        print("高桥")
    elif taka < aoki:
        print("青木")
    else:
        print("画")
run()
