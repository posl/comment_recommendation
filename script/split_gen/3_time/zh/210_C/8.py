def main():
    n, k = map(int, input().split())
    c = list(map(int, input().split()))
    #print(c)
    #print(n, k)
    #print(c[0])
    #print(c[n-1])
    #print(c[n-1] - c[0])
    if n == k:
        print(1)
    else:
        print(n - k + 1)
