def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.insert(0,0)
    b = [0]*(n+1)
    for i in range(1,n+1):
        b[a[i]] += 1
    for i in range(1,n+1):
        print(b[i])
