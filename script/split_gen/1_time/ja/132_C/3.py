def main():
    n = int(input())
    ds = [int(x) for x in input().split()]
    ds.sort()
    print(ds[n//2] - ds[n//2-1])
