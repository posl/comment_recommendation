def main():
    A,B,C,D,E,F,X = map(int, input().split())
    takahashi = 0
    aoki = 0
    for _ in range(X):
        if takahashi % (A+B) < A:
            takahashi += 1
        else:
            takahashi = 0
        if aoki % (D+E) < D:
            aoki +=

if __name__ == '__main__':
    main()