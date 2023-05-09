def main():
    N, M = map(int, input().split())
    party = []
    for i in range(M):
        party.append(list(map(int, input().split()))[1:])
    for i in range(N):
        for j in range(N):
            if i==j:
                continue
            for k in range(M):
                if i+1 in party[k] and j+1 in party[k]:
                    break
            else:
                print('No')
                return
    print('Yes')

if __name__ == '__main__':
    main()