def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    tickets = [0] * 40
    for i in range(M):
        tickets[int(input())] += 1
    for i in range(39):
        tickets[i+1] += tickets[i] // 2
    ans = 0
    for i in range(N):
        ans += A[i] // (2 ** tickets[i])
    print(ans)

if __name__ == '__main__':
    main()