def main():
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    b = []
    for i in range(n-k):
        b.append(a[i+k-1]-a[i])
    if min(b) <= 0:
        print("Yes")
    else:
        print("No")
