def main():
    N, M = map(int, input().split())
    party = [set(map(int, input().split()[1:])) for _ in range(M)]
    for i in range(M):
        for j in range(i + 1, M):
            if len(party[i] & party[j]) == 0:
                print("No")
                return
    print("Yes")

if __name__ == '__main__':
    main()