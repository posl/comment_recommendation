def get_max_sum(N, K, V):
    max_sum = 0
    for i in range(N+1):
        for j in range(N+1):
            if i+j > N:
                continue
            if i+j > K:
                continue
            sum = 0
            l = []
            for k in range(i):
                l.append(V[k])
            for k in range(N-j, N):
                l.append(V[k])
            l.sort()
            for k in range(K-i-j):
                if k < len(l) and l[k] < 0:
                    l[k] = 0
            for k in range(len(l)):
                sum += l[k]
            if sum > max_sum:
                max_sum = sum
    return max_sum
N, K = map(int, input().split())
V = list(map(int, input().split()))
print(get_max_sum(N, K, V))

if __name__ == '__main__':
    get_max_sum()