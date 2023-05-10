def main():
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    q = k//n
    r = k%n
    for i in range(n):
        if i < r:
            print(q+1)
        else:
            print(q)
