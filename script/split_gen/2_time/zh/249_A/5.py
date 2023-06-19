def main():
    A, B, C, D, E, F, X = map(int, input().split())
    time = 0
    while True:
        if time % (A + B) < A:
            X -= E
        else:
            X -= F
        if X <= 0:
            print("青木")
            break
        if time % (D + E) < D:
            X -= C
        else:
            X -= F
        if X <= 0:
            print("高桥")
            break
        time += 1
main()
