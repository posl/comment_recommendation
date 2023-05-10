def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    print(p)
    for i in range(k-1, n):
        print(p[i-k+1:i+1])
