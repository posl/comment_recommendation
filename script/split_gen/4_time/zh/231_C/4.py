def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = [int(input()) for _ in range(q)]
    a.sort()
    for i in range(q):
        for j in range(n):
            if x[i] <= a[j]:
                print(n - j)
                break
