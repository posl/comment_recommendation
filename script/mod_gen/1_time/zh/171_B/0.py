def problems171_b():
    n,k = map(int,input().split())
    p = list(map(int,input().split()))
    p.sort()
    print(sum(p[:k]))

if __name__ == '__main__':
    problems171_b()