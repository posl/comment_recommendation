def main():
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    for i in range(k):
        a[b[i]-1] = 0
    if max(a) == 0:
        print("No")
    else:
        print("Yes")
