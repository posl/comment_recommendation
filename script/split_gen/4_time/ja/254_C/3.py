def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    if n == k:
        if a == sorted(a):
            print("Yes")
        else:
            print("No")
        return
    for i in range(0, n - k):
        if a[i] > a[i + k]:
            print("No")
            return
    print("Yes")
    return
