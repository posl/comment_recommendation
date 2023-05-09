def main():
    x,y,n = map(int, input().split())
    result = n * x
    for i in range(n + 1):
        result = min(result, i * y + (n - i) * x)
    print(result)
