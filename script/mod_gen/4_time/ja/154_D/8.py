def main():
    N, K = map(int, input().split())
    p_list = list(map(int, input().split()))
    p_list = [0] + p_list
    sum_list = [0]
    for i in range(N):
        sum_list.append(sum_list[i] + p_list[i+1])
    max_sum = 0
    for i in range(N-K+1):
        max_sum = max(max_sum, sum_list[i+K] - sum_list[i])
    print((max_sum + K) / 2)

if __name__ == '__main__':
    main()