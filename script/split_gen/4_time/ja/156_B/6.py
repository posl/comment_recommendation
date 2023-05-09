def main():
    n,k = map(int,input().split())
    l = 0
    while n >= k:
        n = n // k
        l += 1
    print(l+1)
