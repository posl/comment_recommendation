def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    min_num = min(a)
    index = a.index(min_num)
    if index < k:
        result = 1 + (k-1)//(k-index)
    else:
        result = 1 + (index-k)//(k-1)
    print(result)
