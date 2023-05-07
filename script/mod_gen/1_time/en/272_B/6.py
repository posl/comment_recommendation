def main():
    N, M = map(int, input().split())
    parties = []
    for i in range(M):
        parties.append(list(map(int, input().split()))[1:])
    # print(parties)
    for i in range(N):
        for j in range(N):
            if i != j:
                flag = False
                for party in parties:
                    if i+1 in party and j+1 in party:
                        flag = True
                        break
                if not flag:
                    print("No")
                    exit()
    print("Yes")

if __name__ == '__main__':
    main()