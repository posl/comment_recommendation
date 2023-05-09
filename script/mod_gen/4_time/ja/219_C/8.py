def main():
    X = input()
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    #print(X)
    #print(N)
    #print(S)
    #print( len(S[0]) )
    #X = list('zyxwvutsrqponmlkjihgfedcba')
    #S = ['a','ab','abc','ac','b']
    #X = list('bacdefghijklmnopqrstuvwxzy')
    #S = ['abx','bzz','bzy','caa']
    X = list(X)
    S = sorted(S)
    #print(X)
    #print(S)
    X_dic = {}
    for i in range(len(X)):
        X_dic[X[i]] = i
    #print(X_dic)
    S_dic = {}
    for s in S:
        tmp = []
        for i in range(len(s)):
            tmp.append( X_dic[s[i]] )
        S_dic[s] = tmp
    #print(S_dic)
    S_dic_sorted = sorted(S_dic.items(), key=lambda x:x[1])
    #print(S_dic_sorted)
    for s in S_dic_sorted:
        print(s[0])
main()

if __name__ == '__main__':
    main()