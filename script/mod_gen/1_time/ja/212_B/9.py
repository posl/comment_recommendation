def main():
    # input
    X = input()
    
    # compute
    if ((X[0]==X[1]==X[2]==X[3]) or (int(X[0])==int(X[1])-1==int(X[2])-2==int(X[3])-3) or (int(X[0])==9 and int(X[1])==0 and int(X[2])==1 and int(X[3])==2)):
        ans = 'Weak'
    else:
        ans = 'Strong'
    
    # output
    print(ans)

if __name__ == '__main__':
    main()