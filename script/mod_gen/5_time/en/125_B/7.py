def max_profit(N, V, C):
    profit = 0
    for i in range(N):
        if V[i] > C[i]:
            profit += V[i] - C[i]
    return profit
N = int(input())
V = list(map(int, input().split()))
C = list(map(int, input().split()))
print(max_profit(N, V, C))

if __name__ == '__main__':
    max_profit()