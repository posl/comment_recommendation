def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    C = [list(map(int, input().split())) for _ in range(M)]
    ans = 0
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if i == j:
                    continue
                if i == k or j == k:
                    continue
                ans += min([C[l] for l in range(M) if AB[l][0] == i+1 and AB[l][1] == j+1])
    print(ans)
main()
I got WA on this code. What is the problem?
I have a problem with the following code:

if __name__ == '__main__':
    main()