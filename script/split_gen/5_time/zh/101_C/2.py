def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    min_num = 10**9
    for i in range(n-k+1):
        if a[i] < a[i+k-1]:
            min_num = min(min_num,a[i])
        else:
            min_num = min(min_num,a[i+k-1])
    print(min_num)
