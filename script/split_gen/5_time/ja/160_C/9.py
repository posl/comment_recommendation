def main():
    k, n = map(int, input().split())
    a = list(map(int, input().split()))
    a.append(a[0]+k)
    max_dist = 0
    for i in range(n):
        max_dist = max(max_dist, a[i+1]-a[i])
    print(k-max_dist)
