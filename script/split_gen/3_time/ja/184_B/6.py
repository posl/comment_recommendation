def main():
    N, X = map(int, input().split())
    S = input()
    for i in S:
        if i == 'o':
            X += 1
        elif i == 'x':
            if X > 0:
                X -= 1
    print(X)
