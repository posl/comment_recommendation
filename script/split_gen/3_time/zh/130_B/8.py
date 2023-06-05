def main():
    n,x = map(int,input().split())
    l = list(map(int,input().split()))
    sum = 0
    for i in range(n):
        sum += l[i]
        if sum > x:
            print(i+1)
            break
    else:
        print(n+1)
