def main():
    N, M = map(int, input().split())
    s = [0] * M
    c = [0] * M
    for i in range(M):
        s[i], c[i] = map(int, input().split())
    #print(N,M,s,c)
    for i in range(10**(N-1), 10**N):
        #print(i)
        flag = True
        for j in range(M):
            if int(str(i)[s[j]-1]) != c[j]:
                flag = False
                break
        if flag:
            print(i)
            return
    print(-1)
    return
