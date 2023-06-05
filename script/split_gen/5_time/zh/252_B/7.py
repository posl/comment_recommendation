def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.sort()
    b.sort()
    for i in range(k):
        if a[n-1] == b[i]:
            print("No")
            exit()
    print("Yes")
