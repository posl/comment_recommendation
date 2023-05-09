def main():
    n = int(input())
    S = [list(input()) for i in range(n)]
    T = [list(input()) for i in range(n)]
    #print(S)
    #print(T)
    for i in range(4):
        if S == T:
            print('Yes')
            break
        else:
            #print('No')
            S = rotate(S)
            #print(S)
    else:
        print('No')
