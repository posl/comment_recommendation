def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    s = sum(a)
    for i in range(m):
        if a[i] * 4 * m < s:
            print("No")
            return
    print("Yes")
