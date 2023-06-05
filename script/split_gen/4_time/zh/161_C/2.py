def main():
    n,k = map(int,input().split())
    if n >= k:
        n = n%k
    if n > k/2:
        n = k-n
    print(n)
