def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(k):
        b[a[i]-1] += 1
    for i in range(n):
        print(b[i])
