def main():
    X = int(input())
    #print(X)
    for i in range(10**5):
        for j in range(10**5):
            if i**5-j**5 == X:
                print(i,j)
                return
            elif i**5-j**5 == -X:
                print(-i,j)
                return

if __name__ == '__main__':
    main()