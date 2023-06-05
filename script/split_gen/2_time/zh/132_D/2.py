def main():
    n = int(input())
    d = list(map(int, input().split()))
    d = sorted(d)
    print(d[n//2] - d[n//2-1])
