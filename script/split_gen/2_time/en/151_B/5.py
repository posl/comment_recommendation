def main():
    n,k,m = map(int,input().split())
    a = list(map(int,input().split()))
    ave = m*n-sum(a)
    if ave <= 0:
        print(0)
    elif ave > k:
        print(-1)
    else:
        print(ave)
