def main():
    ans = -1
    N, M = map(int, input().split())
    #print(N, M)
    sc = [list(map(int, input().split())) for i in range(M)]
    #print(sc)
    for i in range(10**(N-1), 10**N):
        #print(i)
        for j in range(M):
            #print(i, sc[j][0], sc[j][1])
            if int(str(i)[sc[j][0]-1]) != sc[j][1]:
                break
        else:
            ans = i
            break
    print(ans)
    return
