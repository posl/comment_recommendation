def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    min_index = a.index(min(a))
    if min_index <= k-1:
        print(1)
    else:
        print((n-2)//(k-1)+1)
