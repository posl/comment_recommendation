def read_ints():
    return list(map(int, input().split()))
N, C = read_ints()
plans = [read_ints() for _ in range(N)]
plans.sort(key=lambda x:x[0])

if __name__ == '__main__':
    read_ints()