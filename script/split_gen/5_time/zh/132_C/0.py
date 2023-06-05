def main():
    n = int(input())
    d = list(map(int, input().split()))
    d.sort(reverse=True)
    print(d[n//2] - d[n//2 - 1])
