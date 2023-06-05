def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    sum_a = sum(a)
    a.sort(reverse=True)
    if a[m-1]*4*m >= sum_a:
        print('Yes')
    else:
        print('No')
