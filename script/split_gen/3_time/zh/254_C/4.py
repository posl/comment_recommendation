def main():
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    if n == k:
        print("No")
        return
    for i in range(n-k):
        if a[i] > a[i+k]:
            print("Yes")
            return
    print("No")
