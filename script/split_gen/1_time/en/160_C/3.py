def main():
    k, n = map(int, input().split())
    a = list(map(int, input().split()))
    a.append(k+a[0])
    d = [a[i+1]-a[i] for i in range(n)]
    print(k - max(d))
