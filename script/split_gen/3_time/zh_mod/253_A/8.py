def main():
    a = list(map(int, input().split()))
    a.sort()
    if a[1] == a[0] + a[2]:
