def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    t = k//n
    r = k%n
    for i in range(n):
        if i < r:
            print(t+1)
        else:
            print(t)
