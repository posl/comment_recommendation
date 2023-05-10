def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    result = []
    for i in range(n):
        if a[i] != x:
            result.append(a[i])
    print(*result)
