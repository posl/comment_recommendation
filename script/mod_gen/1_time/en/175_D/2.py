def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))
    ans = -10**9
    for i in range(N):
        cycle = []
        j = i
        while True:
            cycle.append(C[j])
            j = P[j]-1
            if j == i:
                break
        cycle_sum = sum(cycle)
        cycle_len = len(cycle)
        cycle_max = max(cycle)
        if cycle_sum > 0:
            cycle_time = min(K//cycle_len, (K-cycle_len)//cycle_len+1)
            ans = max(ans, cycle_sum*cycle_time+cycle_max)
        else:
            cycle_time = min(K//cycle_len, (K-cycle_len)//cycle_len+1)
            ans = max(ans, cycle_sum*cycle_time)
    print(ans)

if __name__ == '__main__':
    main()