def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    cnt = 0
    if (n-1) % (k-1) == 0:
        cnt = (n-1) // (k-1)
    else:
        cnt = (n-1) // (k-1) + 1
    print(cnt)
