def main():
    n,t = map(int,input().split())
    a = list(map(int,input().split()))
    t = t % sum(a)
    sum_a = 0
    for i in range(n):
        sum_a += a[i]
        if sum_a > t:
            print(i+1,t)
            break
