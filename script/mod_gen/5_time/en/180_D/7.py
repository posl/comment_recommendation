def main():
    X, Y, A, B = map(int, input().split())
    exp = 0
    while (X*A) < (X+B) and (X*A) < Y:
        X *= A
        exp += 1
    exp += (Y-1-X)//B
    print(exp)

if __name__ == '__main__':
    main()