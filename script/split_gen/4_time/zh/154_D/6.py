def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    p.sort()
    sum = 0
    for i in p[n-k:n]:
        sum += i
    print((sum+k)/2)
