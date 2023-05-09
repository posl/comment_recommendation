def main():
    n,m = map(int,input().split())
    x = list(map(int,input().split()))
    x.sort()
    if n >= m:
        print(0)
        exit()
    else:
        diff = []
        for i in range(1,m):
            diff.append(x[i] - x[i-1])
        diff.sort()
        print(sum(diff[:m-n]))
