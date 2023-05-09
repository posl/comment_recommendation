def main():
    X, Y, Z = map(int, input().split())
    if X > Y:
        print(-1)
    else:
        print(Z + Y)

if __name__ == '__main__':
    main()