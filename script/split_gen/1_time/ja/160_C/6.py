def main():
    k, n = map(int, input().split())
    a = list(map(int, input().split()))
    diff = []
    for i in range(n):
        if i == n - 1:
            diff.append(k - a[i] + a[0])
        else:
            diff.append(a[i + 1] - a[i])
    print(k - max(diff))
