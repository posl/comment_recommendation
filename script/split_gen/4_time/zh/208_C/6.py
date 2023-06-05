def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    if n >= k:
        for i in range(n):
            print(k//n)
    else:
        for i in range(n):
            print(k//n)
        for i in range(k%n):
            print(1)
