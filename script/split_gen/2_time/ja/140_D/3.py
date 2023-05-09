def main():
    N, K = map(int, input().split())
    S = input()
    LR = []
    for i in range(N):
        if i == 0:
            LR.append([S[i], 1])
        elif S[i] == LR[-1][0]:
            LR[-1][1] += 1
        else:
            LR.append([S[i], 1])
    if len(LR) == 1:
        print(N)
        return
    if LR[0][0] == "R":
        LR.insert(0, ["L", 0])
    if LR[-1][0] == "L":
        LR.append(["R", 0])
    ans = 0
    for i in range(0, len(LR), 2):
        ans += LR[i][1] + LR[i+1][1]
    if len(LR) // 2 <= K:
        print(N)
        return
    for i in range(1, len(LR), 2):
        if i // 2 > K:
            break
        tmp = 0
        for j in range(i, len(LR), 2):
            tmp += LR[j][1] + LR[j+1][1]
            if j // 2 + (len(LR)-j-1) // 2 > K:
                break
        ans = max(ans, tmp)
    print(ans)
