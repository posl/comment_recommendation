def main():
    n, k, q = map(int, input().split())
    a = list(map(int, input().split()))
    l = list(map(int, input().split()))
    for i in range(q):
        a[l[i] - 1] += 1
    for j in range(k):
        if a[j] - q > 0:
            print(j + 1)
