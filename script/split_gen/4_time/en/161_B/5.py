def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    total = sum(a)
    print("Yes" if a[m-1] >= total / (4*m) else "No")
