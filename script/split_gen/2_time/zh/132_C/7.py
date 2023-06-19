def main():
    n = int(input())
    d = list(map(int, input().split()))
    d.sort()
    k = d[n//2-1]
    print(d[n//2]-k)
