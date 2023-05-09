def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(k):
        if i < n:
            a[i] = 0
        else:
            a.append(0)
    print(*a)
