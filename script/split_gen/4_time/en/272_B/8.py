def main():
    n,m = map(int,input().split())
    party = []
    for i in range(m):
        party.append(list(map(int,input().split())))
    party.sort()
    for i in range(m):
        for j in range(i+1,m):
            if len(set(party[i][1:]+party[j][1:])) == n:
                print("NO")
                return
    print("YES")
    return
