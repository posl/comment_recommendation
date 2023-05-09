def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        a,b = [int(_) for _ in input().split()]
        S.append((a,b))
    for i in range(N):
        c,d = [int(_) for _ in input().split()]
        T.append((c,d))
    S.sort(key=lambda x: (x[0], x[1]))
    T.sort(key=lambda x: (x[0], x[1]))
    #print(S)
    #print(T)
    for i in range(N):
        for j in range(N):
            if S[i] == T[j]:
                for k in range(N):
                    S[k] = (S[k][0]-S[i][0], S[k][1]-S[i][1])
                    T[k] = (T[k][0]-T[j][0], T[k][1]-T[j][1])
                break
        else:
            continue
        break
    #print(S)
    #print(T)
    for i in range(N):
        for j in range(N):
            if S[i] == T[j]:
                continue
            else:
                break
        else:
            continue
        break
    else:
        print("Yes")
        return
    print("No")
    return
