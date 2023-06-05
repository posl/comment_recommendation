def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    sum_a = sum(a)
    if sum_a > n:
        print(-1)
    else:
        print(n - sum_a)
