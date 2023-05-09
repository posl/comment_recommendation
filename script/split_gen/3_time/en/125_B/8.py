def main():
    N = int(input())
    values = list(map(int, input().split()))
    costs = list(map(int, input().split()))
    max_value = 0
    for i in range(N):
        if values[i] > costs[i]:
            max_value += values[i] - costs[i]
    print(max_value)
