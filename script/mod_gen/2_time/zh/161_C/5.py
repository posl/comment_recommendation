def problems161_b():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort(reverse=True)
    s = sum(a)
    if a[m-1] >= s/(4*m):
        print("是")
    else:
        print("否")

if __name__ == '__main__':
    problems161_b()