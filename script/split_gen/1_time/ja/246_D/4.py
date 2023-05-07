def main():
    N = int(input())
    if N == 0:
        print(0)
        return
    X = 1
    while True:
        if X**3 >= N:
            print(X)
            return
        X += 1
