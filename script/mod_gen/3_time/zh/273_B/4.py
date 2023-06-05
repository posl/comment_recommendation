def main():
    X,K=map(int,input().split())
    for i in range(K):
        if X%10!=0:
            X+=1
        else:
            X=X//10
    print(X)

if __name__ == '__main__':
    main()