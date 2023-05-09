def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = [abs(a[i] - b[i]) for i in range(n)]
    if max(c) > k:
        print("No")
        return
    if sum(c) % 2 == k % 2:
        print("Yes")
    else:
        print("No")
