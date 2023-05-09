def main():
    N, M = map(int, input().split())
    parties = []
    for _ in range(M):
        parties.append(list(map(int, input().split()))[1:])
    parties = sorted(parties, key=lambda x: len(x))
    for i in range(len(parties)):
        for j in range(i+1, len(parties)):
            if len(set(parties[i]+parties[j])) == N:
                print('No')
                return
    print('Yes')
