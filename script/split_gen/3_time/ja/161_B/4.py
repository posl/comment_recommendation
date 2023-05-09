def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    b = sum(a) / (4 * m)
    for i in range(m):
        if a[i] < b:
            print("No")
            return
    print("Yes")
