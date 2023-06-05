def main():
    L, Q = map(int, input().split())
    querys = []
    for _ in range(Q):
        querys.append(list(map(int, input().split())))
    #print(querys)
    #print(L, Q)
    #print(querys[0][0])
    #print(querys[0][1])
    #print(querys[1][0])
    #print(querys[1][1])
    ans = []
    for i in range(Q):
        if querys[i][0] == 1:
            ans.append(querys[i][1])
        elif querys[i][0] == 2:
            if querys[i][1] in ans:
                ans.remove(querys[i][1])
            else:
                ans.append(L - querys[i][1])
    for i in range(len(ans)):
        print(ans[i])
