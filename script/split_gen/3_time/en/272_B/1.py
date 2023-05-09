def main():
    N, M = map(int, input().split())
    parties = [set(map(int, input().split())) for _ in range(M)]
    for i in range(N):
        for j in range(i + 1, N):
            if not any(i + 1 in party and j + 1 in party for party in parties):
                print("No")
                return
    print("Yes")
main()
