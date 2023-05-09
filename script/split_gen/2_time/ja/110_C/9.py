def main():
    S = input()
    T = input()
    #print(S, T)
    S = list(S)
    T = list(T)
    #print(S, T)
    S.sort()
    T.sort()
    #print(S, T)
    if S == T:
        print('Yes')
    else:
        print('No')
