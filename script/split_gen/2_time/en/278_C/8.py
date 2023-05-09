def main():
    N, Q = map(int, input().split())
    pairs = []
    for i in range(Q):
        pairs.append(list(map(int, input().split())))
    #print(pairs)
    ans = []
    for i in range(Q):
        if pairs[i][0] == 3:
            if pairs[i][1] == pairs[i][2]:
                ans.append("Yes")
            else:
                ans.append("No")
        else:
            if pairs[i][0] == 1:
                pairs[i][0] = 2
            else:
                pairs[i][0] = 1
            for j in range(Q):
                if pairs[j][0] == 3:
                    if pairs[j][1] == pairs[i][1] and pairs[j][2] == pairs[i][2]:
                        ans.append("Yes")
                    elif pairs[j][1] == pairs[i][1] and pairs[j][2] == pairs[i][2]:
                        ans.append("Yes")
                    else:
                        ans.append("No")
    for i in range(len(ans)):
        print(ans[i])
