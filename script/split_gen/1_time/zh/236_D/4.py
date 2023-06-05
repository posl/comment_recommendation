def main():
    n = int(input())
    A = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        A[i] = list(map(int, input().split()))
    result = 0
    for i in range(1, 2 ** (n - 1)):
        people = [0] * n
        for j in range(n):
            if (i >> j) & 1:
                people[j] = 1
        count = 0
        for j in range(n):
            for k in range(j + 1, n):
                if people[j] == 1 and people[k] == 1:
                    count += A[j][k]
        result = max(result, count)
    print(result)
