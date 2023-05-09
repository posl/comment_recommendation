def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    max = 0
    for i in range(0, n):
        if max < a[i]:
            max = a[i]
    for i in range(0, k):
        if max == b[i]:
            print("Yes")
            return
    print("No")
