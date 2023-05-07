def main():
    N, M = map(int, input().split())
    parties = [list(map(int, input().split())) for _ in range(M)]
    people = set([i for i in range(1, N + 1)])
    for party in parties:
        people &= set(party[1:])
    print('Yes' if len(people) == N else 'No')
