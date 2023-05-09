def main():
    N, M = map(int, input().split())
    party = []
    for i in range(M):
        party.append(list(map(int, input().split())))
    for i in range(M):
        for j in range(M):
            if i == j:
                continue
            for k in range(party[i][0]):
                if party[i][k+1] in party[j]:
                    print("Yes")
                    return
    print("No")
