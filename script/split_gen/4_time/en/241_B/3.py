def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if n < m:
        print("No")
        exit()
    a.sort()
    b.sort()
    for i in range(m):
        if a[i] > b[i]:
            print("No")
            exit()
    print("Yes")
