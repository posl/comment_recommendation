def main():
    #入力
    N,A,X,Y=map(int,input().split())
    #キャベツを買う
    if N<=A:
        print(N*X)
    else:
        print(A*X+(N-A)*Y)

if __name__ == '__main__':
    main()