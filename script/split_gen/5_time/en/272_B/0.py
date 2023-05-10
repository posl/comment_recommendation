def main():
    N, M = map(int, input().split())
    parties = []
    for i in range(M):
        parties.append(list(map(int, input().split()))[1:])
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            for party in parties:
                if i+1 not in party or j+1 not in party:
                    break
            else:
                print("Yes")
                return
    else:
        print("No")
