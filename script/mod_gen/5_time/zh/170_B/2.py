def main():
    X,Y = map(int,input().split())
    for i in range(X+1):
        if 2*i + 4*(X-i) == Y:
            print("Yes")
            break
    else:
        print("No")

if __name__ == '__main__':
    main()