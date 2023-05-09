def jog(A,B,C,D,E,F,X):
    #高橋君の距離
    T = 0
    #青木君の距離
    A = 0
    for i in range(X):
        if i%A == 0:
            T += B
        if i%D == 0:
            A += E
    if T > A:
        print("Takahashi")
    elif T < A:
        print("Aoki")
    else:
        print("Draw")
    return
