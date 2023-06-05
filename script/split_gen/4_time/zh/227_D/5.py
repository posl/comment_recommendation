def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    a.reverse()
    #print(a)
    sum = 0
    for i in range(k):
        sum += a[i]
    print(sum)
