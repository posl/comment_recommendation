def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    sum_list = [0]
    for i in range(N):
        sum_list.append(sum_list[i] + A[i])
    for i in range(N):
        for j in range(i + 1, N + 1):
            if sum_list[j] - sum_list[i] == K:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()