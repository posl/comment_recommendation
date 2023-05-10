def solve():
    N, M = map(int, input().split())
    parties = []
    for _ in range(M):
        parties.append(set(map(int, input().split()[1:])))
    for i in range(M):
        for j in range(i+1, M):
            if parties[i] & parties[j]:
                parties[i] |= parties[j]
                parties[j] = set()
    if all(parties):
        print("Yes")
    else:
        print("No")
solve()
