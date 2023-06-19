def main():
    n = int(input())
    p = list(map(int,input().split()))
    q = list(map(int,input().split()))
    # print(p,q)
    a = 0
    b = 0
    for i in range(n):
        a += p[i]*(n-i)
        b += q[i]*(n-i)
    print(abs(a-b))
