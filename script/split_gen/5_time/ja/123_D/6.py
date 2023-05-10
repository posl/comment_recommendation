def main():
    x,y,z,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = list(map(int,input().split()))
    ab = [a[i]+b[j] for i in range(x) for j in range(y)]
    ab.sort(reverse=True)
    abc = [ab[i]+c[j] for i in range(k) for j in range(z)]
    abc.sort(reverse=True)
    for i in range(k):
        print(abc[i])
