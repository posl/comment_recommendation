def solve():
    N,K = map(int,input().split())
    h = list(map(int,input().split()))
    print(len(list(filter(lambda x: x >= K, h))))
