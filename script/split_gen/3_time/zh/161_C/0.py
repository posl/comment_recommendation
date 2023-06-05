def main():
    n, k = map(int, input().split())
    while True:
        if n > abs(n-k):
            n = abs(n-k)
        else:
            print(n)
            break
