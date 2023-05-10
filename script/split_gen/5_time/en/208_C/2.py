def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    result = [k // n] * n
    k %= n
    for i in range(k):
        result[i] += 1
    for i in range(n):
        print(result[i])
