def main():
    N, M = map(int, input().split())
    parties = []
    for i in range(M):
        parties.append(list(map(int, input().split()))[1:])
    for i in range(N):
        for j in range(i+1, N):
            if not (i+1 in parties[j] and j+1 in parties[i]):
                print("No")
                return
    print("Yes")

if __name__ == '__main__':
    main()