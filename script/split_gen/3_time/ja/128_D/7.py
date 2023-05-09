def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    max_value = 0
    for i in range(min(N+1, K+1)):
        for j in range(min(N+1, K+1)-i):
            values = []
            for k in range(i):
                values.append(V[k])
            for k in range(j):
                values.append(V[N-1-k])
            values.sort()
            for k in range(min(K-i-j, len(values))):
                if values[k] < 0:
                    values[k] = 0
            max_value = max(max_value, sum(values))
    print(max_value)
