def main():
    N, M = map(int, input().split())
    party = []
    for i in range(M):
        x = list(map(int, input().split()))
        party.append(x[1:])
    for i in range(N):
        for j in range(i + 1, N):
            flag = False
            for k in party:
                if i + 1 in k and j + 1 in k:
                    flag = True
                    break
            if not flag:
                print("No")
                return
    print("Yes")

if __name__ == '__main__':
    main()