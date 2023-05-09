def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if m > n:
        print("No")
    else:
        a.sort()
        b.sort()
        for i in range(m):
            if a[i] < b[i]:
                print("No")
                exit()
        print("Yes")
