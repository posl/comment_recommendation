def main():
    n = int(input())
    s = list(map(int, input().split()))
    t = list(map(int, input().split()))
    result = [0 for _ in range(n)]
    for i in range(n):
        result[i] = t[i]
    for i in range(1, n):
        result[i] = min(result[i-1]+s[i-1], result[i])
    for i in range(n):
        print(result[i])
