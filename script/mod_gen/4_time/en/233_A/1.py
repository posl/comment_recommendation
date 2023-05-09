def main():
    X,Y = map(int,input().split())
    if X >= Y:
        print(0)
    else:
        print(Y-X)

if __name__ == '__main__':
    main()