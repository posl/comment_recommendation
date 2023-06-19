def main():
    X,Y,N = map(int,input().split())
    if X*3 < Y:
        print(X*N)
    else:
        print(Y*(N//3)+min(X*(N%3),Y))
main()
