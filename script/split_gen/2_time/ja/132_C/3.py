def main():
    N = int(input())
    d = list(map(int, input().split()))
    d.sort()
    K = d[N//2]
    print(K - d[N//2-1])
