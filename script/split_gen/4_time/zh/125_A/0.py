def main():
    a,b,t=map(int,input().split())
    sum=0
    for i in range(1,t+1):
        if i%a==0:
            sum+=b
    print(sum)
