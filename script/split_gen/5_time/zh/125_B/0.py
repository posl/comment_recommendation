def main():
    n = int(input())
    V = [int(i) for i in input().split()]
    C = [int(i) for i in input().split()]
    max_value = 0
    for i in range(1 << n):
        value = 0
        cost = 0
        for j in range(n):
            if (i >> j) & 1:
                value += V[j]
                cost += C[j]
        max_value = max(max_value, value - cost)
    print(max_value)
