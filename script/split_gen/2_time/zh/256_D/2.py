def main():
    N = int(input())
    #S = []
    #for i in range(N):
    #    S.append(input().split())
    #print(S)
    #S.sort(key=lambda x:x[0])
    #print(S)
    #k = 0
    #while k < len(S) - 1:
    #    if S[k][1] >= S[k+1][0]:
    #        S[k][1] = max(S[k][1],S[k+1][1])
    #        del S[k+1]
    #    else:
    #        k += 1
    #for i in range(len(S)):
    #    print(S[i][0],S[i][1])
    #S = []
    #for i in range(N):
    #    S.append(input().split())
    #print(S)
    #S.sort(key=lambda x:x[0])
    #print(S)
    #k = 0
    #while k < len(S) - 1:
    #    if S[k][1] >= S[k+1][0]:
    #        S[k][1] = max(S[k][1],S[k+1][1])
    #        del S[k+1]
    #    else:
    #        k += 1
    #for i in range(len(S)):
    #    print(S[i][0],S[i][1])
    S = []
    for i in range(N):
        S.append(input().split())
    S.sort(key=lambda x:x[0])
    k = 0
    while k < len(S) - 1:
        if S[k][1] >= S[k+1][0]:
            S[k][1] = max(S[k][1],S[k+1][1])
            del S[k+1]
        else:
            k += 1
    for i in range(len(S)):
        print(S[i][0],S[i][1])
