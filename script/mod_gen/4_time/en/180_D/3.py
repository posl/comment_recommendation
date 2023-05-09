def main():
    X, Y, A, B = map(int, input().split())
    exp = 0
    while A*X <= X+B and A*X < Y:
        X *= A
        exp += 1
    exp += (Y-X-1)//B
    print(exp)

if __name__ == '__main__':
    main()