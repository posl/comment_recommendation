def main():
    N, M = map(int, input().split())
    parties = [set(map(int, input().split()[1:])) for _ in range(M)]
    for i in range(N):
        for j in range(i + 1, N):
            for party in parties:
                if i + 1 in party and j + 1 in party:
                    break
            else:
                print('No')
                return
    print('Yes')
