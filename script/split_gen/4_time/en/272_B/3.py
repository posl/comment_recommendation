def main():
    N, M = map(int, input().split())
    party = []
    for i in range(M):
        party.append(list(map(int, input().split()))[1:])
    for i in range(N):
        for j in range(i+1, N):
            if not any([i+1 in p and j+1 in p for p in party]):
                print("No")
                return
    print("Yes")
