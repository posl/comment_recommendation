def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    i = 0
    while k > 0:
        i = a[i] - 1
        k -= 1
    print(i+1)
