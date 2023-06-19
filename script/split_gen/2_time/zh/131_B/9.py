def main():
    n,l=map(int,input().split())
    min=1000000
    sum=0
    for i in range(n):
        sum+=l+i
        if abs(l+i)<abs(min):
            min=l+i
    print(sum-min)
