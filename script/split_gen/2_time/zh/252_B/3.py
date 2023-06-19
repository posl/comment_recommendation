def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    for i in range(k):
        for j in range(n):
            if a[j] == b[i]:
                a[j] = 0
    if max(a) == 0:
        print("No")
    else:
        print("Yes")
