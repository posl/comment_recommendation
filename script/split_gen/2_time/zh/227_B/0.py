def main():
    n,k,a = map(int,input().split())
    if k < n:
        print(k+a)
    else:
        k = k-n
        a = a-1
        print((a+k)%n+1)
