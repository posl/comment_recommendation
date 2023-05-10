def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    diff = 0
    for i in range(n):
        diff += abs(a[i]-b[i])
    if k >= diff and (k-diff)%2 == 0:
        print("Yes")
    else:
        print("No")
