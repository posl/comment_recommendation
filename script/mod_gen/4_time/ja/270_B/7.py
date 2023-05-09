def main():
    X,Y,Z = map(int,input().split())
    if X > Y:
        print(Z)
    else:
        print(-1)

if __name__ == '__main__':
    main()