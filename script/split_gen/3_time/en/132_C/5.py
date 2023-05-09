def main():
    N = int(input())
    d = list(map(int, input().split()))
    d.sort()
    k = d[N//2]
    print(k - d[N//2 - 1])
