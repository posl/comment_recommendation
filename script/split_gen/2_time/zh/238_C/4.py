def main():
    n = int(input())
    a = list(map(int, input().split()))
    result = 0
    for i in range(n):
        now = 0
        for j in range(n):
            now += a[(i + j) % n]
            result = max(result, now)
    print(360 - result)
