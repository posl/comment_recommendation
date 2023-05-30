def main():
    N, M = map(int, input().split())
    S = [list(map(int, input().split()))[1:] for _ in range(M)]
    ans = 'No'
    for i in range(N):
        for j in range(i+1, N):
            if all(i+1 in x and j+1 in x for x in S):
                ans = 'Yes'
    print(ans)
main()
