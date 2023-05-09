def main():
    S = input()
    T = input()
    if S == T:
        print(0)
        return
    S = list(S)
    T = list(T)
    #print(S)
    #print(T)
    for i in range(len(S)):
        #print(i)
        if S == T:
            print(i)
            return
        else:
            S.append(S.pop(0))
            #print(S)
    print(-1)
    return
