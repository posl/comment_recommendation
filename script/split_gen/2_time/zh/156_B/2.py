def main():
    n,k = map(int,input().split())
    i = 0
    while n >= k:
        n = n // k
        i += 1
    print(i+1)
