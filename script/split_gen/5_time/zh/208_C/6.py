def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    cnt = k//n
    rem = k%n
    for i in range(n):
        if i < rem:
            print(cnt+1)
        else:
            print(cnt)
