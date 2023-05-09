def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    ans = []
    for i in range(N):
        if S[i] not in S[:i]:
            ans.append(S[i])
        else:
            count = 1
            for j in range(i-1,-1,-1):
                if S[i] == S[j]:
                    count += 1
                else:
                    break
            ans.append(S[i] + '(' + str(count-1) + ')')
    for i in range(N):
        print(ans[i])
