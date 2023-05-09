def main():
    X,K = map(int,input().split())
    X = list(str(X))
    X.reverse()
    for i in range(K):
        if int(X[i]) >= 5:
            if i == K-1:
                X[i] = "0"
                X.append("1")
            else:
                X[i] = "0"
                X[i+1] = str(int(X[i+1])+1)
    X.reverse()
    print("".join(X))
