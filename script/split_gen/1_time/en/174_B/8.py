def main():
    # Enter your code here. Read input from STDIN. Print output to STDOUT
    import math
    N,D=map(int,input().split())
    count=0
    for i in range(N):
        X,Y=map(int,input().split())
        if math.sqrt(X**2+Y**2)<=D:
            count+=1
    print(count)
