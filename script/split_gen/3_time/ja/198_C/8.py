def main():
    R, X, Y = map(int, input().split())
    X = abs(X)
    Y = abs(Y)
    if X <= R and Y <= R:
        print(2)
    else:
        count = 0
        while True:
            if X <= R and Y <= R:
                break
            else:
                X -= R
                Y -= R
                count += 1
        print(count)
