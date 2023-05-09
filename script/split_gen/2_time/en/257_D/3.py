def main():
    N = int(input())
    X = [0]*N
    Y = [0]*N
    P = [0]*N
    for i in range(N):
        x, y, p = map(int, input().split())
        X[i] = x
        Y[i] = y
        P[i] = p
    #print(X)
    #print(Y)
    #print(P)
    S = 0
    while True:
        for i in range(N):
            for j in range(N):
                if i != j:
                    if P[i]*S < abs(X[i]-X[j])+abs(Y[i]-Y[j]):
                        break
                if j == N-1:
                    print(S)
                    return
        S += 1
main()
I have a problem with the following code. It is not working correctly. It is not able to find the correct answer. Can anyone please help me in this?
I have a problem with the following code. It is not working correctly. It is not able to find the correct answer. Can anyone please help me in this?
I have a problem with the following code. It is not working correctly. It is not able to find the correct answer. Can anyone please help me in this?
I have a problem with the following code. It is not working correctly. It is not able to find the correct answer. Can anyone please help me in this?
I have a problem with the following code. It is not working correctly. It is not able to find the correct answer. Can anyone please help me in this?
I have a problem with the following code. It is not working correctly. It is not able to find the correct answer. Can anyone please help me in this?
I have a problem with the following code. It is not working correctly. It is not able to find the correct answer. Can anyone please help me in this?
I have a problem with the following code. It is not working correctly. It is not able to find the correct answer. Can anyone please help me in this?
I have a problem with the following code. It is not working correctly. It is not able to find the correct answer. Can anyone please help me in this?
I have a problem with the following code. It is not working correctly. It is not able to find the correct answer. Can anyone please help me in this?
I have a problem
