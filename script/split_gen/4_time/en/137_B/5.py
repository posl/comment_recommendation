def main():
    K,X = map(int,input().split())
    if K == 1:
        print(X)
    else:
        for i in range(X-(K-1),X+(K-1)+1):
            print(i,end=" ")