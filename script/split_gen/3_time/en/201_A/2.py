def main():
    a = list(map(int, input().split()))
    a.sort()
    print("Yes" if a[2] - a[1] == a[1] - a[0] else "No")
