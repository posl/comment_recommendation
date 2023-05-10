def main():
    # N = int(input())
    # X = [0 for _ in range(N)]
    # Y = [0 for _ in range(N)]
    # for i in range(N):
    #     X[i],Y[i] = map(int,input().split())
    #     # print(X[i],Y[i])
    # for i in range(N):
    #     for j in range(i+1,N):
    #         for k in range(j+1,N):
    #             if (Y[i]-Y[j])*(X[i]-X[k]) == (Y[i]-Y[k])*(X[i]-X[j]):
    #                 print("Yes")
    #                 return
    # print("No")
    N = int(input())
    X = [0 for _ in range(N)]
    Y = [0 for _ in range(N)]
    for i in range(N):
        X[i],Y[i] = map(int,input().split())
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                if (Y[i]-Y[j])*(X[i]-X[k]) == (Y[i]-Y[k])*(X[i]-X[j]):
                    print("Yes")
                    return
    print("No")
