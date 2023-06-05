def shiritori(N, W):
    if len(W) != N:
        return "No"
    else:
        for i in range(1, N):
            if W[i][0] != W[i-1][-1]:
                return "No"
        if len(set(W)) != N:
            return "No"
        else:
            return "Yes"
N = int(input())
W = []
for i in range(N):
    W.append(input())
print(shiritori(N, W))
