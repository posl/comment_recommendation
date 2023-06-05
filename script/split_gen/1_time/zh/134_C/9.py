def main():
    n=int(input())
    a=[]
    for i in range(n):
        a.append(int(input()))
    for i in range(n):
        b=a[0:i]+a[i+1:n]
        print(max(b))
