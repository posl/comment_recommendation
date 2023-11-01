def run(A,B,C,D,E,F,X):
    time = 0
    while X > 0:
        if A > 0:
            X -= B
            time += A
            if X <= 0:
                return "Takahashi"
        X -= C
        if X <= 0:
            return "Takahashi"
        if D > 0:
            X -= E
            time += D
            if X <= 0:
                return "Aoki"

if __name__ == '__main__':
    run()