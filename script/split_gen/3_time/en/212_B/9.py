def main():
    #input
    X = input()
    #compute
    if X[0]==X[1]==X[2]==X[3]:
        ans = 'Weak'
    elif int(X[1])-int(X[0]) == 1 and int(X[2])-int(X[1]) == 1 and int(X[3])-int(X[2]) == 1:
        ans = 'Weak'
    elif int(X[1])-int(X[0]) == -9 and int(X[2])-int(X[1]) == -9 and int(X[3])-int(X[2]) == -9:
        ans = 'Weak'
    else:
        ans = 'Strong'
    #output
    print(ans)
