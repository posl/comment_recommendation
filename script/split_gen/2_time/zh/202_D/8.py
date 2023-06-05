def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int,input().split()))
    #print(n,a,b,c)
    d = [0] * n
    for i in range(n):
        d[c[i]-1] += 1
    #print(d)
    e = [0] * n
    for i in range(n):
        e[b[c[i]-1]-1] += 1
    #print(e)
    sum = 0
    for i in range(n):
        sum += d[i] * e[i]
    print(sum)
