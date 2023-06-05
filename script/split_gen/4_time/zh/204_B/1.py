def main():
    n = int(input())
    a = list(map(int, input().split()))
    result = 0
    for i in range(n):
        if a[i] > 10:
            result += a[i] - 10
    print(result)
