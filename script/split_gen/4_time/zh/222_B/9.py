def main():
    #input
    n,p = map(int,input().split())
    a = list(map(int,input().split()))
    #count
    count = 0
    for i in range(n):
        if a[i] < p:
            count += 1
    #output
    print(count)
