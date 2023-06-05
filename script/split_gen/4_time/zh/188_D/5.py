def read_ints():
    return list(map(int, input().split()))
N, C = read_ints()
plans = [read_ints() for _ in range(N)]
plans.sort(key=lambda x:x[0])
